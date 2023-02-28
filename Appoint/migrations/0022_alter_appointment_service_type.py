# Generated by Django 4.1.3 on 2023-02-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0021_alter_appointment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service_type',
            field=models.CharField(choices=[('haircut', 'Haircut'), ('coloring', 'Coloring'), ('styling', 'Styling'), ('nail', 'Nail Services'), ('other', 'Other')], max_length=100),
        ),
    ]
