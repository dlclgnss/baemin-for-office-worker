from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import PartnerForm,MenuForm
from .models import Partner,Menu



#기본페이지 (로그인한 업체정보를 보여준다.)
def index(request):
    if request.method == 'POST':
        partner_form = PartnerForm(request.POST)
        if partner_form.is_valid():
            partner=partner_form.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect("index")
    else:
        partner_form = PartnerForm()

    ctx={
        'partner_form':partner_form
        }
    return render(request,'index.html',ctx)



#업체정보 수정 (정보를 가져오는 인스턴스 값을 추가하면된다.)
def edit_info(request):
    if request.method == 'POST':
        partner_form = PartnerForm(request.POST,instance=request.user.partner)
        if partner_form.is_valid():
            partner=partner_form.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect("index")
    else:
        partner_form = PartnerForm(instance=request.user.partner)

    ctx={
        'partner_form':partner_form
        }

    return render(request,'edit_info.html',ctx)


# 로그인 하는 페이지
def signin(request):
    ctx={}
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: # 유저가 존재 한다면
            login(request, user)
            return redirect("index")
        else:
            ctx.update({'error':'아이디 및 비밀번호가 잘못되었습니다.'})


    return render(request,'login.html',ctx)



# 로그아웃 하는 페이지
def signout(request):
    logout(request)
    return redirect("index")


# 회원가입 하는 페이지
def signup(request):
    ctx={}
    if request.method == 'POST':
        username =request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #create_user를 이용해서 아이디 이메일 비번을 저장한다.
        user = User.objects.create_user(username,email,password)
        return redirect('index')
    return render(request,'signup.html',ctx)



#메뉴 추가페이지
def menu_add(request):
    if request.method == 'POST':
        menu_form = MenuForm(request.POST,request.FILES)
        if menu_form.is_valid():
            menu=menu_form.save(commit=False)
            menu.partner = request.user.partner
            menu.save()
            return redirect("menu")
    else:
        menu_form = MenuForm()

    ctx={
        'menu_form':menu_form
        }
    return render(request,'menuadd.html',ctx)



#메뉴페이지
def menu(request):
    menu_list = Menu.objects.filter(partner = request.user.partner)
    ctx={
    'menu_list':menu_list
    }
    return render(request,'menu.html',ctx)


#메뉴 상세페이지
def menu_detail(request, menu_id):
    menu=Menu.objects.get(id = menu_id)
    ctx={'menu': menu}
    return render(request,'menu_detail.html',ctx)


#메뉴 상세페이지에서 수정하기
def menu_edit(request, menu_id):
    # menu=Menu.objects.get(id = menu_id)
    menu=get_object_or_404(Menu,id = menu_id)
    if request.method == 'POST':
        menu_form = MenuForm(request.POST,request.FILES, instance=menu)
        if menu_form.is_valid():
            menu=menu_form.save(commit=False)
            menu.partner = request.user.partner
            menu.save()
            return redirect("menu_detail",menu.id)
    else:
        menu_form = MenuForm(instance=menu)

    ctx={
        'menu_form':menu_form,
        'replace':'수정',
        }

    return render(request,'menuadd.html',ctx)


#메뉴목록하나 삭제하기
def menu_delete(request, menu_id):
    menu=get_object_or_404(Menu,id = menu_id)
    menu.delete()

    return redirect('menu')
