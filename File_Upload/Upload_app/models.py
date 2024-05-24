from django.db import models

# Create your models here.
class Myfileupload(models.Model):
    file_name=models.CharField(max_length=33)
    file=models.FileField()

