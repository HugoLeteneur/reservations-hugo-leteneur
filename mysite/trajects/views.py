from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ReservationForm
from .models import Trajet, Reservation, Client
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def trajets(request):
    trajets_disponibles = Trajet.objects.all()
    return render(request, 'reservations/trajets.html', {'trajets': trajets_disponibles})

def trajets_redirect(request):
    return redirect('trajects')


@login_required
def reservations(request):
    reservations_utilisateur = Reservation.objects.filter(client=request.user.client)
    return render(request, 'reservations/reservations.html', {'reservations': reservations_utilisateur})

@login_required
def reservation_detail(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    return render(request, 'reservations/reservation.html', {'reservation': reservation})

@login_required
def profile(request):
    return render(request, 'reservations/profile.html')

@login_required
def nouvelle_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Récupérer l'identifiant du client actuellement authentifié
            client_id = request.user.id
            
            # Créer une nouvelle réservation avec l'identifiant du client
            reservation = form.save(commit=False)
            reservation.client_id = client_id
            reservation.save()

            # Rediriger l'utilisateur vers la page de ses réservations
            return redirect('trajects:reservation')
    else:
        form = ReservationForm()
    
    context = {
        'form': form,
        # Vous pouvez passer d'autres données nécessaires pour le formulaire
        'trajets': Trajet.objects.all()  # Supposons que Trajet soit le modèle pour les trajets
    }
    return render(request, 'trajects/nouvelle_reservation.html', context)