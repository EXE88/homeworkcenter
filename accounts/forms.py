from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50 , required=True , widget=forms.TextInput(attrs={}))
    email = forms.EmailField(required=True , widget=forms.EmailInput(attrs={}))
    password = forms.CharField(required=True , widget=forms.PasswordInput(attrs={}))
    password_verify = forms.CharField(required=True , widget=forms.PasswordInput(attrs={}))
    
    def validate_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email
    
    def clean(self):
        cd =  super().clean()
        password = cd.get('password')
        password_verify = cd.get('password_verify')
        
        if password and password_verify and password != password_verify:
            raise ValidationError('the passwords must be match')
        