from django.shortcuts import render
from rest_framework.views import APIView
from . import forms

class CreateNewHomework(APIView):
    def get(self,request):
        return render(request,'homework/createnewhomework.html')