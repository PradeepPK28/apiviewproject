from django.db import models

# Create your models here.


class empdetails(models.Model):
    name = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone_no = models.IntegerField()
