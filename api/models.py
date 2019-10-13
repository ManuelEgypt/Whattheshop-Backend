from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField()
    price = models.TextField()
    duration = models.CharField(max_length=10)
    destination = models.TextField()
    # tours = models.TextField()
    
