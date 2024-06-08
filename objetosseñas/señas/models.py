from django.db import models

# Create your models here.
class Señas(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sign_images/')

    def __str__(self):
        return self.name