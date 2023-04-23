
#Creation des vues
from django.shortcuts import render
from .models import Vin
from datetime import datetime

# Create your views here.
'''def index(request):
    vins = Vin.objects.all()
    vins_names_and_region = [vin.nom + " / " + vin.region for vin in vins]
    vins_names_str = ", ".join(vins_names_and_region)
    return HttpResponse("<h1>Ma premiere application web : </h1>" + vins_names_str) 
'''
def index(request):
    return render(request, "menu/index.html")

def article(request, numero_article):
    return render(request, f"menu/article_{numero_article}.html")



