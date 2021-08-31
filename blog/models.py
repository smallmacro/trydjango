from django.db import models
from django.urls import reverse
# Create your models here.
# using class based  views



class Article(models.Model):
     """docstring for ClassName"""
    
     title       =      models.CharField(max_length=200)
     author      =      models.CharField(max_length=120)
     edit_time   =      models.DateTimeField(auto_now=False)
     content     =      models.TextField()

     def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"pk": self.id})