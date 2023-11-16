from django.shortcuts import render,redirect , get_object_or_404
from django.contrib import messages
from django.views import View
from . import forms
from . import models
from jdatetime import date

class CreateNewHomework(View):
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
        
class EditHomework(View):
    form_class = forms.EditHomeworkForm
    
    def get(self, request, postid):
        self.post_instance = get_object_or_404(models.WriteHomework, pk=postid)
        form = self.form_class(instance=self.post_instance)
        return render(request, 'homework/edithomeworkpage.html', {"form": form})

    def post(self, request, postid):
        self.post_instance = get_object_or_404(models.WriteHomework, pk=postid)
        form = self.form_class(request.POST, instance=self.post_instance)
        
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.save()
            messages.success(request,'homework updated successfully','success')
            return redirect('main_page')    
        messages.error(request,'something went wrong','danger')
        return redirect('main_page')