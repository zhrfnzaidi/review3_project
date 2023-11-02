from django.db import models

# Create your models here.

class Review(models.Model):
   name = models.TextField()
   text = models.TextField()
