from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(default='null')
    summary = models.TextField(default='null')
    numOfRead = models.IntegerField(default=0)
    numOfComment = models.IntegerField(default=0)
    ownerId = models.IntegerField(default=0)
