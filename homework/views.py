from django.shortcuts import render,redirect , get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from jdatetime import date

class CreateNewHomework(LoginRequiredMixin,View):
    form_class = forms.WriteHomeworkForm
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request,'فقط ادمین ها اجازه دسترسی به این بخش را دارند','danger')
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)

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
            more_description = cd['more_description']
            )
            messages.success(request,'با موفقیت ثبت شد','success')
            return redirect('main_page')
        
class EditHomework(LoginRequiredMixin,View):
    form_class = forms.EditHomeworkForm
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(models.WriteHomework, pk=kwargs['postid'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request,'فقط ادمین ها اجازه دسترسی به این بخش را دارند','danger')
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)
     
    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'homework/edithomeworkpage.html', {"form": form})

    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.save()
            messages.success(request,'با موفقیت آپدیت شد','success')
            return redirect('main_page')    
        messages.error(request,'مشکلی پیش آمده است','danger')
        return redirect('main_page')
    
class DeleteHomework(LoginRequiredMixin,View):
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(models.WriteHomework,pk=kwargs['postid'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request,'فقط ادمین ها اجازه دسترسی به این بخش را دارند','danger')
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,*args, **kwargs):
        return render(request,'homework/deletehomeworkpage.html')
    
    def post(self,request,*args, **kwargs):
        post = self.post_instance
        post.delete()
        messages.success(request,'با موفقیت حذف شد','success')
        return redirect('main_page')