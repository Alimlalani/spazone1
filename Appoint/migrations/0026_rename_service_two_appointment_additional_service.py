# Generated by Django 4.1.3 on 2023-02-24 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0025_appointment_service_two'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='service_two',
            new_name='Additional_service',
        ),
    ]
