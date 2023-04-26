from django.db import models

# Create your models here.
class Vin(models.Model):
    nom = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    couleur = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    producteur = models.CharField(max_length=200)
    millesime = models.IntegerField(default=0)
    quantite = models.IntegerField(default=0)
    date_ajout = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom