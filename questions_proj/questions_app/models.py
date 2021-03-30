from django.db import models


class Questions(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
