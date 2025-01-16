from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os
from django.conf import settings

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=255, unique=True)
    media_directory = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"

def set_media_diretory (sender, instance, **kwargs):
    if not instance.media_directory:
        instance.media_directory = os.path.join (settings.RADIO_MEDIA_URL, instance.name)

