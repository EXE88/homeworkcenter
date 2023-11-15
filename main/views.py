from django.shortcuts import render , redirect
from django.views import View
from homework import models
from jdatetime import date
from datetime import timedelta
from googletrans import Translator

class MainPage(View):
    def get(self,request):
        allmodels = models.WriteHomework.objects.all()
        for model in allmodels:
            miladi_date = date(year=model.date.year,month=model.date.month,day=model.date.day).togregorian()
            shamsi_date = date.fromgregorian(year = miladi_date.year , month = miladi_date.month , day = miladi_date.day)
            model.date = f"{shamsi_date.year}/{shamsi_date.month}/{shamsi_date.day} {shamsi_date.strftime('%A')}"
            #translator = Translator()
            #model.date = translator.translate(text=model.date,dest='fa',src='en').text 
        sorted_models = sorted(allmodels, key=lambda x: x.date, reverse=True)
        return render(request,'main/mainpage.html',{"models":sorted_models})