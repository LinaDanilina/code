# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    product_description = models.CharField(max_length=1000)

