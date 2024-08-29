from django import forms
from .models import User

class MyForm(forms.Form):
    pseudo_name = forms.CharField(max_length=15)
    password = forms.CharField(max_length=225)
    creat_at = forms.DateTimeField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pseudo_name', 'password', 'creat_at']
        exclude = ['creat_at']  


