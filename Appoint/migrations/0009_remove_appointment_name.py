# Generated by Django 4.1.3 on 2023-02-24 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0008_alter_appointment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Name',
        ),
    ]
