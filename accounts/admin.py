from django.contrib import admin
from . import models

@admin.register(models.UserVerifyCode)
class UserVerifyCodeAdmin(admin.ModelAdmin):
    pass