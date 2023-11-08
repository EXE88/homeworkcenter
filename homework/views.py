from django.shortcuts import render
from rest_framework.views import APIView
from . import forms

class CreateNewHomework(APIView):
    form_class = forms.WriteHomeworkForm
    def get(self,request):
        form = self.form_class()
        return render(request,'homework/createnewhomework.html',{"form":form,"day":form.tomorrow.strftime('%A')})