# Generated by Django 4.1.3 on 2023-02-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoint', '0030_remove_appointment_time_slot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Additional_service',
            new_name='sub_service',
        ),
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone_no',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
