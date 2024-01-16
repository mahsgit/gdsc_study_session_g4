from django.db import models
from BlogApp.models import Post

class Comment(models.Model):
    Content=models.TextField( max_length='80')
    Author=models.CharField(max_length=100)
    PublishedDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    Post=models.ForeignKey(Post, on_delete=models.CASCADE)