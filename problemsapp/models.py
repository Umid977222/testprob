from datetime import datetime

from django.db import models

# Create your models here.


def upload_location(instance, filename):
    return filename


class Problems(models.Model):
    product_model = models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to=upload_location, default='posts/default.jpg')
    description = models.TextField()
    add_bot_button = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
