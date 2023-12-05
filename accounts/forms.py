from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):
    
    grade_choices = (
        (0,'نهم 1'),
        (1,'نهم 2'),
        (2,'نهم 3'),
        (4,'هشتم 1'),
        (5,'هشتم 2'),
        (6,'هشتم 3'),
        (7,'هشتم 4'),
        (8,'هفتم 1'),
        (8,'هفتم 2'),
        (9,'هفتم 3'),
        (10,'هفتم 4'),
    )
    
    username = forms.CharField(max_length=25 , label='نام کاربری' , required=True , widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(required=True  , label='ایمیل' , widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True , label='رمز عبور' , widget=forms.PasswordInput(attrs={"class":"form-control"}) , max_length=15 , min_length=8)
    password_verify = forms.CharField(required=True , label='تایید رمزعبور' , widget=forms.PasswordInput(attrs={"class":"form-control"}) , max_length=15 , min_length=8)
    grade = forms.ChoiceField(choices=grade_choices , required=True , label='پایه' , widget=forms.Select(attrs={'class':'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError('this email already exists')
        return email
    
    def clean(self):
        cd =  super().clean()
        password = cd.get('password')
        password_verify = cd.get('password_verify')
        username = cd.get('username')
        
        username_exists = User.objects.filter(username=username).exists()
        if password and password_verify and password != password_verify:
            raise ValidationError('the passwords must be match')
        if username_exists:
            raise ValidationError('there is a user with this username')
        
class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}) , label='ایمیل')
    password = forms.CharField(max_length=15,min_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}) , label='رمزعبور')
    
class UserEmailVeifyForm(forms.Form):
    verifycode = forms.CharField(min_length=6,max_length=6, required=True ,label='کد تایید' ,widget=forms.TextInput(attrs={'class':'form-control'}))