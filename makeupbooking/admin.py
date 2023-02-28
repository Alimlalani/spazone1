# In admin.py
from django.contrib import admin
from Appoint.models import Appointment,MyformModel

admin.site.register(Appointment)
admin.site.register(MyformModel)