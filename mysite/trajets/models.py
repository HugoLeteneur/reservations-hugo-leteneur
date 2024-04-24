from django.db import models
from django.contrib.auth.models import User

class Gare(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom}"

class Trajet(models.Model):
    gare_depart = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name='trajets_depart')
    gare_arrivee = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name='trajets_arrivee')

    def __str__(self):
        return f"{self.gare_depart} - {self.gare_arrivee}"
    

    
class Reservation(models.Model):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)  # Assurez-vous d'avoir importé le modèle Trajet si nécessaire
    numero_place = models.IntegerField()
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='client',default=None)
    

    def __str__(self):
        return f"Réservation {self.id} - {self.trajet.gare_depart} à {self.trajet.gare_arrivee}"
  

class Passager(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
  