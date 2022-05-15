from django.db import models
from django.forms import CharField

# Create your models here.
class MovieDetail(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=8)
    released = models.CharField(max_length=50)
    imdbrating = models.CharField(max_length=4)