from django.shortcuts import render
from .forms import user_reg
from .forms import MembersReg


def reg(request):
    submit_button = request.POST.get("jhbe")
    name = ''
    email = ''
    password = ''

    reg_form = user_reg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context = {'reg_form': reg_form, 'name': name, 'email': email, 'submit_button': submit_button}
    return render(request, 'register.html', context)


def reg_members(request):
    submit_members = request.POST.get("members")
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''

    reg_members = MembersReg(request.POST or None)
    if reg_members.is_valid():
        name = reg_members.cleaned_data.get("name")
        age = reg_members.cleaned_data.get("age")
        phone = reg_members.cleaned_data.get("phone")
        city = reg_members.cleaned_data.get("city")
        country = reg_members.cleaned_data.get("country")
    context = {'reg_members': reg_members,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'country': country,
               'submit_members': submit_members}
    return render(request, 'members.html', context)
