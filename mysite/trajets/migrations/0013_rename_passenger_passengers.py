# Generated by Django 4.2 on 2024-04-25 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trajets', '0012_reservation_passenger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passenger',
            new_name='Passengers',
        ),
    ]
