from django.shortcuts import render,redirect , get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from jdatetime import date
from datetime import timedelta , datetime

class CreateNewHomework(LoginRequiredMixin,View):
    form_class = forms.WriteHomeworkForm
    template_name  = 'homework/createnewhomeworkpage.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request,'فقط ادمین ها اجازه دسترسی به این بخش را دارند','danger')
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        current_time = datetime.now()
        current_solar_time = date.fromgregorian(year=current_time.year,month=current_time.month,day=current_time.day)
        
        if 'Thursday' in current_solar_time.strftime('%A'):
            tomorrow = datetime.now() + timedelta(days=2)
            tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
            form.fields['date'].initial = tomorrow
        
        elif 'Friday' in current_solar_time.strftime('%A'):
            tomorrow = datetime.now() + timedelta(days=1)
            tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
            form.fields['date'].initial = tomorrow 
            
        else:
            tomorrow = datetime.now() + timedelta(days=1)
            tomorrow = date.fromgregorian(year = tomorrow.year , month = tomorrow.month , day = tomorrow.day)
            form.fields['date'].initial = tomorrow 
        
        for group in request.user.groups.all():
            group = str(group)
            
            if "ninth grade class 1" in group:
                form.fields['grade'].initial = "نهم 1"
                
            if "ninth grade class 2" in group:
                form.fields['grade'].initial = "نهم 2"
                
            if "ninth grade class 3" in group:
                form.fields['grade'].initial = "نهم 3" 
                               
            if "eighth grade class 1" in group:
                form.fields['grade'].initial = "هشتم 1" 
                               
            if "eighth grade class 2" in group:
                form.fields['grade'].initial = "هشتم 2"
                
            if "eighth grade class 3" in group:
                form.fields['grade'].initial = "هشتم 3"
                
            if "eighth grade class 4" in group:
                form.fields['grade'].initial = "هشتم 4" 
                
            if "seventh grade class 1" in group:
                form.fields['grade'].initial = "هفتم 1"                 
                                                               
            if "seventh grade class 2" in group:
                form.fields['grade'].initial = "هفتم 2"
                
            if "seventh grade class 3" in group:
                form.fields['grade'].initial = "هفتم 3"
                
            if "seventh grade class 4" in group:
                form.fields['grade'].initial = "هفتم 4"                                                                                               
                                                               
        return render(request, self.template_name, {"form":form,"day":tomorrow.strftime('%A')})
   
    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_homework = models.WriteHomework.objects.create(
                date = cd['date'],
                grade = cd['grade'],
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
    template_name = 'homework/edithomeworkpage.html'
    
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
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.save()
            messages.success(request,'با موفقیت بروز رسانی شد','success')
            return redirect('main_page')    
        messages.error(request,'مشکلی پیش آمده است','danger')
        return redirect('main_page')
    
class DeleteHomework(LoginRequiredMixin,View):
    template_name = 'homework/deletehomeworkpage.html'
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(models.WriteHomework,pk=kwargs['postid'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request,'فقط ادمین ها اجازه دسترسی به این بخش را دارند','danger')
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request, *args, **kwargs):
        post = self.post_instance
        post.delete()
        messages.success(request,'با موفقیت حذف شد','success')
        return redirect('main_page')