from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Gare(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom}"

class Trajet(models.Model):
    gare_depart = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name='trajets_depart')
    gare_arrivee = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name='trajets_arrivee')

    def __str__(self):
        return f"{self.gare_depart} - {self.gare_arrivee}"
    
class Passengers(models.Model):
    prenom = models.CharField(max_length=30, default="PB DE PASSAGER")
    nom = models.CharField(max_length=30,default="")

    def __str__(self):
        return f"{self.prenom}"
    

class Reservation(models.Model):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)  # Assurez-vous d'avoir importé le modèle Trajet si nécessaire
    numero_place = models.IntegerField()
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='client',default=None)
    passenger = models.ForeignKey(Passengers, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Réservation {self.id} - {self.trajet.gare_depart} à {self.trajet.gare_arrivee}"
  


