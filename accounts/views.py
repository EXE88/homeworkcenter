from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from . import forms
from django.contrib import messages
from django.shortcuts import redirect , render

class UserRegisterView(APIView):
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
    
class UserLoginView(APIView):
    def get(self,request):
        return render(request,'accounts/loginpage.html')
    def post(self,request):
        pass
    
class UserLogoutView(APIView):
    def get(self,request):
        return render(request,'accounts/logoutpage.html')
    def post(self,request):
        pass
