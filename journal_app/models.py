from django.db import models
import datetime


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='SOME STRING')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class Quotes(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    content = models.TextField(default='SOME QUOTE')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quotes"
