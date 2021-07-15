from django.shortcuts import render, redirect
from django.views import View
from .models import LandLord

# Create your views here.
def index(request):
    tenants = LandLord.objects.all()
    return render(request, 'view_tenants.html', {'tenants': tenants})

class AddTenant(View):
    def get(self,request):
        return render(request, 'add_tenant.html')
    def post(self,request):
        form_data = request.POST.copy()
        db_name = 'db_'+str(form_data.get('subdomain'))
        tenant = LandLord(name=form_data.get('name'), subdomain=form_data.get('subdomain'), db_name=db_name)
        tenant.save()

        return redirect('landlord:index')