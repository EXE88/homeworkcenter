from django import forms
from datetime import datetime , timedelta
from jdatetime import date

class WriteHomeworkForm(forms.Form):
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
    date = forms.DateField(initial=tomorrow , widget=forms.TextInput(attrs={'readonly':False , 'class':'form-control'}))
    math = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    literature = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    biology = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    physics = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    religious = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    Defense_readiness = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    Social_studies = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    english = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    conversation = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    arabic = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    quran = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    writeing = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))
    art = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form-control'}))