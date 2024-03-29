# Generated by Django 4.1.3 on 2023-02-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0031_rename_additional_service_appointment_sub_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyformModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('service_type', models.CharField(max_length=100)),
                ('sub_service', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
