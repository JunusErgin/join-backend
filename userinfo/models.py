from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    group = models.CharField(max_length=6, default='UNSET')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[Gruppe {}] - {}'.format(self.group, self.user)
