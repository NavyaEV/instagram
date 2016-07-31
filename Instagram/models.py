from __future__ import unicode_literals

from django.db import models
#from .storage import AppEngineBlobStorage
# Create your models here.

class imageStore(models.Model):
    image=models.ImageField(upload_to='myfiles')
    status=models.CharField(max_length=200,blank=True, null=True)
