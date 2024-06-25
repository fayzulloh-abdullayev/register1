from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.
def register(request):

    forms = RegisterForm()
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            new_forms = forms.save(commit=False)
            password = forms.cleaned_data.get("password")
            username = forms.cleaned_data.get("first_name")
            phone_number = forms.cleaned_data.get("phone_number")
            forms.cleaned_data.get("email")

            new_forms.set_password(password)
            new_forms.username = username
            new_forms.save()
            return redirect("login")
    return render(request=request, template_name="register.html", context={"forms": forms})
        



def login(request):

    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=phone_number, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "You are soccessed login")
            return redirect("accounts:index")
        else:
            return HttpResponse("Login Failed")
    return render(request, "login.html")
