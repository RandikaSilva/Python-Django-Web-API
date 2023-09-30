from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


def defult_create_date():
    return datetime.now()


class Company(models.Model):
    company_code = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_description = models.CharField(max_length=500)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, null=True)
    adress_line3 = models.CharField(max_length=200, null=True)
    mobile_no1 = models.CharField(max_length=12)
    mobile_no2 = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=defult_create_date)
    created_by = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    update_by = models.IntegerField(null=True)


class CompanyUser(models.Model):
    company_id = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=defult_create_date)
    created_by = models.IntegerField(null=True)
    update_date = models.DateTimeField(null=True)
    update_by = models.IntegerField(null=True)
