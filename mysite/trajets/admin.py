from django.contrib import admin

from .models import Gare
from .models import Trajet
from .models import Reservation
from .models import Passengers

admin.site.register(Gare)
admin.site.register(Trajet)
admin.site.register(Reservation)
admin.site.register(Passengers)