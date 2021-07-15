from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField(auto_now_add=True)
    on_trial = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

class Domain(DomainMixin):
    pass