from django.db import models

class Post(models.Model):
    Title=models.CharField(unique=True, max_length=500)
    Content=models.TextField(max_length=1000)
    Category=models.CharField(max_length=500)
    # Image=models.ImageField()
    # Tags=models.ArrayField(models.CharField(max_length=500))
    