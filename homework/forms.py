from django import forms
from datetime import datetime , timedelta
from jdatetime import date

class WriteHomeworkForm(forms.Form):
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
    date = forms.DateField(initial=tomorrow , widget=forms.TextInput(attrs={'readonly':True , 'class':'form_control'}))
    math = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    literature = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    biology = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    physics = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    religious = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    Defense_readiness = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    Social_studies = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    english = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    conversation = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    arabic = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    quran = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    writeing = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))
    art = forms.CharField(max_length=100 , required=False , widget=forms.TextInput(attrs={'class':'form_control'}))