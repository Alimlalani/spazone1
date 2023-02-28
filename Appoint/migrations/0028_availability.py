# Generated by Django 4.1.3 on 2023-02-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0027_availabletimeslot_appointment_time_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]