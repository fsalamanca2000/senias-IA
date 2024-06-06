from django.db import models

# Create your models here.
class RecognizedObject(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)