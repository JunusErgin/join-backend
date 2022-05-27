from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ("MANAGEMENT", "Management"),
    ("SOFTWARE", "Software Development"),
    ("UXUI", "UX/UI Design"),
    ("OTHER", "Other"),
)


URGENCY_CHOICES = (
    ("HIGH", "High"),
    ("INTERMEDIATE", "Intermediate"),
    ("LOW", "Low"),
)


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    category = models.CharField(max_length=15,
                  choices=CATEGORY_CHOICES,
                  default="OTHER")
    urgency = models.CharField(max_length=15,
                  choices=URGENCY_CHOICES,
                  default="OTHER")
    group = models.CharField(max_length=6, default='UNSET')
    due_date = models.DateField()
    users = models.ManyToManyField(User)