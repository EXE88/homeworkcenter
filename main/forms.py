from django import forms
from datetime import datetime , timedelta
from jdatetime import date

class WriteHomeworkForm(forms.Form):
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
    date = forms.DateField(initial=tomorrow)
    math = forms.CharField(max_length=100)
    literature = forms.CharField(max_length=100)
    biology = forms.CharField(max_length=100)
    physics = forms.CharField(max_length=100)
    religious = forms.CharField(max_length=100)
    Defense_readiness = forms.CharField(max_length=100)
    Social_studies = forms.CharField(max_length=100)
    english = forms.CharField(max_length=100)
    conversation = forms.CharField(max_length=100)
    arabic = forms.CharField(max_length=100)
    quran = forms.CharField(max_length=100)
    writeing = forms.CharField(max_length=100)
    art = forms.CharField(max_length=100)