# from django.db import models
# from django.contrib.auth.models import User

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     password = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name


# class Appointment(models.Model):
#     date = models.DateField()
#     time = models.TimeField()
#     service_type = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.service_type} appointment on {self.date} at {self.time}"

# class Payment(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_method = models.CharField(max_length=100)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.amount} paid by {self.customer.username} for appointment on {self.appointment.date}"


