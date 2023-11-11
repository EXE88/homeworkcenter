from django.contrib import admin
from . import models

@admin.register(models.WriteHomework)
class WriteHomeworkAdmin(admin.ModelAdmin):
    pass

