from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    Onderdeel = models.CharField(max_length=100, null=True, blank=True)
    Reeks = models.TextField()
    content = models.TextField()
    
    #  User hier bij voegen?????







