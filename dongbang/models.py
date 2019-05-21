from django.db import models

class Message(models.Model):
    content = models.TextField()
    writer = models.CharField(max_length = 10)
    date = models.DateField()