# resume/models.py

from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField()
    experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.name

