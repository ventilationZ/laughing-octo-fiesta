from django.shortcuts import render
from .forms import user_reg
def reg(request):
    submit_button = request.POST.get("jhbe")
    name =''
    email =''
    password =''

    reg_form =user_reg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context ={'reg_form':reg_form , 'name':name , 'email': email, 'submit_button' : submit_button}
    return render(request,'register.html',context)