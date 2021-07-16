from django.db import models

# Create your models here.
class CompanyUser(models.Model):
    name = models.CharField(verbose_name='Employee name', max_length=50)
    phone = models.CharField(verbose_name='Employee phone', max_length=50)
    email = models.CharField(verbose_name='Employee email', max_length=50)
    address = models.CharField(verbose_name='Employee address', max_length=50)
    