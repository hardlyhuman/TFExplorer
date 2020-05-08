from django.db import models
from django.db.models import Model
# Create your models here.


class API(Model):
    name = models.CharField('API Name', max_length=256)
    usage = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    link = models.URLField(max_length=256)


class API_Variant(Model):
    api = models.ForeignKey(API, on_delete=models.CASCADE)
    usage = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
