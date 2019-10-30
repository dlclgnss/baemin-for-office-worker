from django import forms
from django.forms import ModelForm
from .models import Partner,Menu

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields  = [
        'name',
        'contact',
        'address',
        'description',
        ]
       #form에는 장고가 제공하는 위젯이라는게 있고 폼마다 내용의 특징을 달리 할 수 있다.
       # 장고 공식문서에서 ModelForm안에는 widgets을 찾아보면된다.
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields  = [
        'image',
        'name',
        'price',
        ]
       #form에는 장고가 제공하는 위젯이라는게 있고 폼마다 내용의 특징을 달리 할 수 있다.
       # 장고 공식문서에서 ModelForm안에는 widgets을 찾아보면된다.
        widgets = {
            # 'image': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.Textarea(attrs={'class':'form-control'}),
        }
