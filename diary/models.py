from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
