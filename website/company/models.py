from django.db import models


# Create your models here.
class Contact_model(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    sensor = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email
