from django.shortcuts import render , redirect
from django.views import View
from homework import models
from jdatetime import date
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin

class MainPage(LoginRequiredMixin,View):
    def get(self,request):
        for group in request.user.groups.all():
            group = str(group)
            if 'ninth grade class 1' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='نهم 1')
                
            if 'ninth grade class 2' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='نهم 2')                
                
            if 'ninth grade class 3' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='نهم 3')
                                
            if 'eighth grade class 1' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هشتم 1') 
                
            if 'eighth grade class 2' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هشتم 2') 
                
            if 'eighth grade class 3' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هشتم 3') 
                                                                               
            if 'eighth grade class 4' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هشتم 4')  
                
            if 'seventh grade class 1' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هفتم 1')                                                                                               
                
            if 'seventh grade class 2' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هفتم 2')
                
            if 'seventh grade class 3' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هفتم 3')
                
            if 'seventh grade class 4' in group:
                allmodels = models.WriteHomework.objects.all().filter(grade='هفتم 4')                                                
                
        for model in allmodels:
            miladi_date = date(year=model.date.year,month=model.date.month,day=model.date.day).togregorian()
            shamsi_date = date.fromgregorian(year = miladi_date.year , month = miladi_date.month , day = miladi_date.day)
            model.date = f"{shamsi_date.year}/{shamsi_date.month}/{shamsi_date.day} {shamsi_date.strftime('%A')}"
            
            full_date = model.date
            if "Saturday" in full_date:
                model.date = full_date.replace('Saturday','شنبه')
            if "Sunday" in full_date:
                model.date = full_date.replace('Sunday','یکشنبه')
            if "Monday" in full_date:
                model.date = full_date.replace('Monday','دوشنبه')
            if "Tuesday" in full_date:
                model.date = full_date.replace('Tuesday','سه شنبه')
            if "Wednesday" in full_date:
                model.date = full_date.replace('Wednesday','چهارشنبه')
            if "Thursday" in full_date:
                shamsi_date_plus_two_days = shamsi_date + timedelta(days=2)
                model.date = full_date = full_date.replace('Thursday','شنبه') 
                model.date = full_date.replace(f'{shamsi_date.year}/{shamsi_date.month}/{shamsi_date.day}',f'{shamsi_date_plus_two_days.year}/{shamsi_date_plus_two_days.month}/{shamsi_date_plus_two_days.day}')    
            if "Friday" in full_date:
                shamsi_date_plus_one_day = shamsi_date + timedelta(days=1)
                model.date  = full_date = full_date.replace('Friday','شنبه')
                model.date = full_date.replace(f'{shamsi_date.year}/{shamsi_date.month}/{shamsi_date.day}',f'{shamsi_date_plus_one_day.year}/{shamsi_date_plus_one_day.month}/{shamsi_date_plus_one_day.day}')
        
        sorted_models = sorted(allmodels, key=lambda x: x.date, reverse=True)
        return render(request,'main/mainpage.html',{"models":sorted_models}) 