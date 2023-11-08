from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework.views import APIView
from . import forms

class CreateNewHomework(APIView):
    form_class = forms.WriteHomeworkForm
    def get(self,request):
        form = self.form_class()
        return render(request,'homework/createnewhomeworkpage.html',{"form":form,"day":form.tomorrow.strftime('%A')})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request,'successful')
            return redirect('main_page')