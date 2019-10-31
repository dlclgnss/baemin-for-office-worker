from django.shortcuts import render
from partner.models import Partner #다른쪽 모델을 가져올때

# Create your views here.
def index(request):
    partner_list=Partner.objects.all()
    ctx={
    'partner_list':partner_list
    }
    return render(request,'main.html',ctx)
