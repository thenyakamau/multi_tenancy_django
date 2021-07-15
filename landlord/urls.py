from django.urls import path
from .views import *

app_name='landlord'

urlpatterns =[
    path('', index, name='index'),
    path('add_tenant', AddTenant.as_view()),
]