from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate , login , logout

class UserRegisterView(View):
    form_class = forms.UserRegisterForm
    template_name = "accounts/registerpage.html"
    def get(self,request):
        form = self.form_class()
        return render(request,'accounts/registerpage.html',{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            messages.success(request,'you are registered successfully','success')
            return redirect('main_page')
        return render(request,self.template_name,{"form":form})
    
class UserLoginView(View):
    form_class = forms.UserLoginForm
    template_name = "accounts/loginpage.html"
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.filter(email=cd['email'])
                username = list(user)
                username = username[0]
            except:
                messages.error(request,'no user exists with this email','warning')
                return render(request,self.template_name,{'form':form})
            user = authenticate(request,username=username,password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you are logged in successfully','success')
                return redirect('main_page')
            messages.error(request,'username or password is wrong','warning')
        return render(request,self.template_name,{'form':form})
    
class UserLogoutView(LoginRequiredMixin,View):
    template_name  = 'accounts/logoutpage.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        logout(request)
        messages.success(request,'you are logged out successfully','success')
        return redirect('main_page')
