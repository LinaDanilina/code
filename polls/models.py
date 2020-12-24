# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Client(models.Model):
    client_surname = models.CharField(max_length=200)
    client_name=models.CharField(max_length=200)
    client_address=models.CharField(max_length=1000)
    client_number=models.BigIntegerField()

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=1000)
    cl = models.ForeignKey(Client, on_delete=models.CASCADE)


class Employee(models.Model):
    emp_surname = models.CharField(max_length=200)
    emp_name = models.CharField(max_length=200)
    emp_position = models.CharField(max_length=1000)
    emp_number=models.BigIntegerField()






