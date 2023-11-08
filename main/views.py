from django.shortcuts import render , redirect
from rest_framework.views import APIView
from . import forms

class MainPage(APIView):
    def get(self,request):
        return render(request,'main/mainpage.html')