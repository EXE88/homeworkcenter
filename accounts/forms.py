from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=25 , required=True , widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(required=True , widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True , widget=forms.PasswordInput(attrs={"class":"form-control"}) , max_length=15 , min_length=8)
    password_verify = forms.CharField(required=True , widget=forms.PasswordInput(attrs={"class":"form-control"}) , max_length=15 , min_length=8)
    
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
        