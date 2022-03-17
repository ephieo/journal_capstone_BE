from django.db import models
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='SOME STRING')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
