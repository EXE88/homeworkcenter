from django.db import models

class WriteHomework(models.Model):
    date = models.DateField(blank=False)
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