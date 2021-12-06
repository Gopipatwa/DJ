from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)