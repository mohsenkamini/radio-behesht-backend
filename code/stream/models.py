from django.db import models

# Create your models here.

class StreamRequest(models.Model):
    STATUS_CHOICES = [
      ('pending', 'Pending'),
      ('in_review', 'In Review'),
      ('accepted', 'Rejected'),
      ('rejected', 'Accepted'),
    ]

    program_name = models.CharField(max_length=255)
    description = models.TextField()
    schedule = models.CharField(max_length=255)
    start_date = models.DateField()
    episodes = models.PositiveIntegerField()
    contact = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return self.program_name




