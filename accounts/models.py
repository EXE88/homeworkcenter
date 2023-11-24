from django.db import models
from django.contrib.auth.models import User

class UserVerifyCode(models.Model):
    username = models.CharField(max_length=50,blank=False)
    verifycode = models.CharField(max_length=6,blank=False)
    
    def __str__(self):
        return self.username