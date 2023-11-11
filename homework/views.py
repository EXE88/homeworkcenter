from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework.views import APIView
from . import forms
from . import models
from jdatetime import date

class CreateNewHomework(APIView):
    form_class = forms.WriteHomeworkForm
    def get(self,request):
        form = self.form_class()
        return render(request,'homework/createnewhomeworkpage.html',{"form":form,"day":form.tomorrow.strftime('%A')})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_homework = models.WriteHomework.objects.create(
            date = cd['date'],
            math = cd['math'],
            literature = cd['literature'],
            biology = cd['biology'],
            physics = cd['physics'],
            religious = cd['religious'],
            Defense_readiness = cd['Defense_readiness'],
            Social_studies = cd['Social_studies'],
            english = cd['english'],
            conversation = cd['conversation'],
            arabic = cd['arabic'],
            quran = cd['quran'],
            writeing = cd['writeing'],
            art = cd['art'],
            )
            messages.success(request,'successful','success')
            return redirect('main_page')