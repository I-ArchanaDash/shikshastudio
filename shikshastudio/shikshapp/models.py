from django.db import models

# Create your models here.

class shikshapp_teachers(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)