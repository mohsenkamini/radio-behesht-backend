from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class RadioUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    profilePicture = models.ImageField(upload_to='static/user/pictures/', null=True, blank=True)
