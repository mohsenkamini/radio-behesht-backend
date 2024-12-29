from django.db import models

# Create your models here.

class StreamRequest(models.Model):
    programName = models.CharField(max_length=255)
    description = models.TextField()
    schedule = models.CharField(max_length=255)
    startDate = models.DateField()
    episodes = models.PositiveIntegerField()
    contact = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.programName




