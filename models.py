from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    user_comment = models.CharField(max_length=200)