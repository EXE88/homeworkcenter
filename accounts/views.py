from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from . import forms

class UserRegisterView(APIView):
    form_class = forms.UserRegisterForm
    def get(self,request):
        form = self.form_class()
        return render(request,'accounts/registerpage.html',{'form':form})
    def post(self,request):
        pass
    
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
