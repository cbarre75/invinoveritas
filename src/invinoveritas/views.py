from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
'''def index(request):
    vins = Vin.objects.all()
    vins_names_and_region = [vin.nom + " / " + vin.region for vin in vins]
    vins_names_str = ", ".join(vins_names_and_region)
    return HttpResponse("<h1>Ma premiere application web : </h1>" + vins_names_str) 
'''
def index(request):
    return render(request, "invinoveritas/index.html", context={"date" : datetime.today()})



