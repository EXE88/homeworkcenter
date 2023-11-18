from django import forms
from datetime import datetime , timedelta
from jdatetime import date
from . import models

class WriteHomeworkForm(forms.Form):
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
    date = forms.DateField(initial=tomorrow , widget=forms.TextInput(attrs={'readonly':True , 'class':'form-control'}))
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
    more_description = forms.CharField(max_length=250,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
    
class EditHomeworkForm(forms.ModelForm):
    class Meta:
        model = models.WriteHomework
        fields = (
                "date",
                "math",
                "literature",
                "biology",
                "physics",
                "religious",
                "Defense_readiness",
                "Social_studies",
                "english",
                "conversation",
                "arabic",
                "quran",
                "writeing",
                "art",
                "more_description"
                )
        widgets = {
            "date" : forms.TextInput(attrs={'readolny':True , 'class':'form-control'}),
            "math" : forms.TextInput(attrs={'class':'form-control'}),
            "literature" : forms.TextInput(attrs={'class':'form-control'}),
            "biology" : forms.TextInput(attrs={'class':'form-control'}),
            "physics" : forms.TextInput(attrs={'class':'form-control'}),
            "religious" : forms.TextInput(attrs={'class':'form-control'}),
            "Defense_readiness" : forms.TextInput(attrs={'class':'form-control'}),
            "Social_studies" : forms.TextInput(attrs={'class':'form-control'}),
            "english" : forms.TextInput(attrs={'class':'form-control'}),
            "conversation" : forms.TextInput(attrs={'class':'form-control'}),
            "arabic" : forms.TextInput(attrs={'class':'form-control'}),
            "quran" : forms.TextInput(attrs={'class':'form-control'}),
            "writeing" : forms.TextInput(attrs={'class':'form-control'}),
            "art" : forms.TextInput(attrs={'class':'form-control'}),
            "more_description" : forms.Textarea(attrs={'class':'form-control'})
        }
        