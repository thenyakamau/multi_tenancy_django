from django.db import models


# Create your models here.
class LandLord(models.Model):
    name = models.CharField(verbose_name='company_name', max_length=50)
    subdomain = models.CharField(verbose_name='sub_domain', max_length=50)
    db_name = models.CharField(verbose_name='database name', max_length=70)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = "landlords"
        verbose_name = "LandLord"
        verbose_name_plural = "LandLords"