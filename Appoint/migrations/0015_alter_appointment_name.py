# Generated by Django 4.1.3 on 2023-02-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0014_appointment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(blank=True, default=1, max_length=20),
        ),
    ]
