from django.contrib import admin

from .models import Client
from .models import Gare
from .models import Trajet
from .models import Reservation

admin.site.register(Client)
admin.site.register(Gare)
admin.site.register(Trajet)
admin.site.register(Reservation)