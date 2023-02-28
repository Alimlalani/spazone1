from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from .models import ServiceType
from django.utils import timezone

class User(AbstractUser):
    class Meta:
        app_label = 'appoint'

class ServiceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Availability(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]
    day = models.CharField(choices=DAY_CHOICES, max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} ({self.start_time} - {self.end_time})"

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"


class AvailableTimeSlot(models.Model):
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} {self.start_time}-{self.end_time}"
class Appointment(models.Model):
    
    SERVICE_TYPE_CHOICES = [
        ('haircut', 'Haircut'),
        ('coloring', 'Coloring'),
        ('styling', 'Styling'),
        ('nail', 'Nail Services'),
        ('other', 'Other'),
    ]
    date = models.DateField()
    name = models.CharField(max_length=50, default='',null=True)
    date = models.DateField(max_length=100)
    time = models.TimeField(max_length=100)
    email =models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=50, default='',null=True)
    service_type = models.CharField(choices=SERVICE_TYPE_CHOICES, max_length=50, null=True, default='')
    sub_service = models.CharField(choices=SERVICE_TYPE_CHOICES, max_length=50, null=True, default='')
    # time_slot = models.ForeignKey(AvailableTimeSlot, on_delete=models.CASCADE,null=True, default='')

    # service_type = models.ManyToManyField(ServiceType)
    # service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    service = models.CharField(max_length=100)  # define the service field
    # location = models.CharField(max_length=100)
    # Name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # class ServiceType(models.Model):
    #     name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.service_type} appointment on {self.date} at {self.time} name {self.name} and {self.email} and {self.sub_service} phone {self.phone_no}"

    
    def get_available_time_slots(date):
    # Get all available time slots for the selected day
            available_time_slots = Availability.objects.filter(day=date.strftime('%A'))

            # Get all booked appointments for the selected date
            booked_appointments = Appointment.objects.filter(date=date)

            # Loop through available time slots and remove any that are already booked
            for appointment in booked_appointments:
                for time_slot in available_time_slots:
                    if time_slot.start_time <= appointment.time < time_slot.end_time:
                        available_time_slots = available_time_slots.exclude(id=time_slot.id)
                        break   

        # Return the remaining available time slots
            return available_time_slots
class MyformModel(models.Model):
    name = models.CharField(max_length=50, default='',null=True)
    email = models.EmailField()
    service_type = models.CharField(max_length=100)
    sub_service = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    phone = models.CharField(max_length=20)
    # form_snippet = models.TextField()

    def __str__(self):
        return self.name


class AppointmentTimeSlot(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointment} - {self.time_slot}"

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)  # define the card_number field
    card_expiry = models.CharField(max_length=5)  # define the card_expiry field
    card_cvv = models.CharField(max_length=3) 
    
    def __str__(self):
        return f"{self.amount} paid by {self.customer.username} for appointment on {self.appointment.date}"
