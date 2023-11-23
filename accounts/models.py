from django.db import models
from django.contrib.auth.models import User

class CoustomUser(User):
    is_verifyed = models.BooleanField(default=False)
