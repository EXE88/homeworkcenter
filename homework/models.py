from django.db import models

class WriteHomework(models.Model):
    date = models.DateField(blank=False)
    grade = models.CharField(max_length=50 , blank=False)
    math = models.CharField(max_length=100 , blank=True)
    literature = models.CharField(max_length=100 , blank=True)
    biology = models.CharField(max_length=100 , blank=True)
    physics = models.CharField(max_length=100 , blank=True)
    religious = models.CharField(max_length=100 , blank=True)
    Defense_readiness = models.CharField(max_length=100 , blank=True)
    Social_studies = models.CharField(max_length=100 , blank=True)
    english = models.CharField(max_length=100 , blank=True)
    conversation = models.CharField(max_length=100 , blank=True)
    arabic = models.CharField(max_length=100 , blank=True)
    quran = models.CharField(max_length=100 , blank=True)
    writeing = models.CharField(max_length=100 , blank=True)
    art = models.CharField(max_length=100 , blank=True)
    more_description = models.TextField(max_length=250,blank=True)
    
    def __str__(self):
        return f"{self.date} - {self.date.strftime('%A')} - {self.grade}"