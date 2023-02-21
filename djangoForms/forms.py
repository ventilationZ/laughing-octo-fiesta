from django import forms

class user_reg(forms.Form):
    name =forms.CharField(max_length=100)
    email =forms.CharField(max_length=100)
    password =forms.CharField()

class user_login(forms.Form)
    username =forms.CharField(max_length=100)
    userpassword =forms.CharField()


