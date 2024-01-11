from django.db import models

# Create your models here.
class Image(models.Model):
    imagename=models.CharField(max_length=100)
    image=models.ImageField(upload_to='imgapp/photos/')
