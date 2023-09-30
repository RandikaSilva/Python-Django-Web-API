from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


def defult_create_date():
    return datetime.now()


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_desciption = models.CharField(max_length=5000)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=defult_create_date)
    created_by = models.CharField(max_length=100)
    update_date = models.DateField(null=True)
    update_by = models.CharField(max_length=100, null=True)
