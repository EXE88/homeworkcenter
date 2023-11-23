from django.contrib import admin
from . import models

@admin.register(models.CoustomUser)
class CoustomUserAdmin(admin.ModelAdmin):
    pass
