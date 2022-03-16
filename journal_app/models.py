from django.db import models
import datetime


class Posts(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def num(digit):
        return digit
