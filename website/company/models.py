from django.db import models

# Create your models here.
class Contact_model(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(unique=True)
    sensor = models.CharField(max_length=264)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.email
