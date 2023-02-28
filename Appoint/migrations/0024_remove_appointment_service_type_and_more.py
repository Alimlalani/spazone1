# Generated by Django 4.1.3 on 2023-02-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0023_servicetype_remove_appointment_service_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='service_type',
        ),
        migrations.AddField(
            model_name='appointment',
            name='service_type',
            field=models.CharField(choices=[('haircut', 'Haircut'), ('coloring', 'Coloring'), ('styling', 'Styling'), ('nail', 'Nail Services'), ('other', 'Other')], default='', max_length=50, null=True),
        ),
    ]