# Generated by Django 4.1.3 on 2023-02-23 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0002_appointment_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Appoint.user'),
        ),
    ]
