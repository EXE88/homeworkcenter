from django import forms
from datetime import datetime , timedelta
from jdatetime import date
from . import models

class WriteHomeworkForm(forms.ModelForm):
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
        labels = {
            "date": "تاریخ",
            "math": "ریاضی",
            "literature": "فارسی",
            "biology": "زیست",
            "physics": "فیزیک",
            "religious": "دینی",
            "Defense_readiness": "آمادگی دفاعی",
            "Social_studies": "مطالعات اجتماعی",
            "english": "زبان",
            "conversation": "مکالمه",
            "arabic": "عربی",
            "quran": "قرآن",
            "writeing": "نگارش",
            "art": "هنر",
            "more_description": "توضیحات اضافه"
        }
    
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
        labels = {
            "date": "تاریخ",
            "math": "ریاضی",
            "literature": "فارسی",
            "biology": "زیست",
            "physics": "فیزیک",
            "religious": "دینی",
            "Defense_readiness": "آمادگی دفاعی",
            "Social_studies": "مطالعات اجتماعی",
            "english": "زبان",
            "conversation": "مکالمه",
            "arabic": "عربی",
            "quran": "قرآن",
            "writeing": "نگارش",
            "art": "هنر",
            "more_description": "توضیحات اضافه"
        }
        