from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'trajets'


urlpatterns = [
    path('', views.trajets_redirect, name='trajets_redirect'),  
    path('trajets/', views.trajets, name='trajets'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('nouvelle_reservation/', views.nouvelle_reservation, name='nouvelle_reservation'),
    path('modif_reservation/<int:reservation_id>/', views.nouvelle_reservation, name='nouvelle_reservation'),
    path('compte/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]