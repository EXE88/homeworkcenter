from django import forms
from datetime import datetime , timedelta
from jdatetime import date

class WriteHomeworkForm(forms.Form):
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
    date = forms.DateField(initial=tomorrow,widget=forms.TextInput(attrs={'readonly':True}))
    math = forms.CharField(max_length=100 , required=False)
    literature = forms.CharField(max_length=100 , required=False)
    biology = forms.CharField(max_length=100 , required=False)
    physics = forms.CharField(max_length=100 , required=False)
    religious = forms.CharField(max_length=100 , required=False)
    Defense_readiness = forms.CharField(max_length=100 , required=False)
    Social_studies = forms.CharField(max_length=100 , required=False)
    english = forms.CharField(max_length=100 , required=False)
    conversation = forms.CharField(max_length=100 , required=False)
    arabic = forms.CharField(max_length=100 , required=False)
    quran = forms.CharField(max_length=100 , required=False)
    writeing = forms.CharField(max_length=100 , required=False)
    art = forms.CharField(max_length=100 , required=False)