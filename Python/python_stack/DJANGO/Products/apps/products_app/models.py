from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    weight = models.FloatField
    price = models.FloatField
    cost = models.FloatField
    category = models.CharField(max_length=100)
