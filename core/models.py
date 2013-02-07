from django.conf import settings
from django.db import models
import os

# Create your models here.
class UploadedImage(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="images")
