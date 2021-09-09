from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=300)
    job_title = models.CharField(max_length=300, blank=True)
    company = models.CharField(max_length=300, blank=True)

