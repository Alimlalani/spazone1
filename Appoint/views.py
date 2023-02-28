from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Appointment, Payment
from .forms import AppointmentForm, PaymentForm
from .models import Appointment, ServiceType, TimeSlot, AppointmentTimeSlot
from django.core.mail import send_mail
from .forms import MyForm

def home(request):
    return render(request, 'makeupbooking/home.html')

def payment(request):
    return render(request, 'makeupbooking/payment.html')
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            # Login the user
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'makeupbooking/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'makeupbooking/login_view.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'makeupbooking/login_view.html')


# @login_required
def book_appointment(request):
    # form=MyForm(request.POST)
    if request.method == 'POST':
        form = MyForm(request.POST)
        # model = MyForm
        # context = {'form': form}
        if form.is_valid():
            # appointment = form.save(commit=True)
            # appointment.customer = request.user # Ensure customer is the currently logged-in user
            # appointment.save()
            form.save(commit=False)
            # send_mail(
            #     'New Appointment Booking',
            #     'A new appointment has been booked.',
            #     'nomiwoh946@wiroute.com', # Replace with your email address
            #     ['nomiwoh946@wiroute.com'], # Replace with your email address
            #     fail_silently=False,
            # )
            # return redirect('success')
            return redirect(('payment'))
        else:
            print(form.errors)
            # form.save()
            return redirect(('register'))
    else:
        form = MyForm()
    return render(request, 'makeupbooking/book_appointment.html',{'form': form})

# @login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(name=request.user)
    context = {'appointments': appointments}
    return render(request, 'makeupbooking/view_appointments.html', context)

@login_required
def manage_appointment(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'makeupbooking/manage_appointment.html', {'form': form})

# @login_required


def process_payment(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user
            payment.appointment = appointment
            payment.save()
            return redirect('appointments')
    else:
        form = PaymentForm()
    return render(request, 'payment/process_payment.html', {'form': form, 'appointment': appointment})

@login_required
def view_payments(request):
    payments = Payment.objects.filter(customer=request.user)
    return render(request, 'payment/view_payments.html', {'payments': payments})

@login_required
def delete_payment(request, pk):
    payment = Payment.objects.get(pk=pk)
    payment.delete()
    return redirect('payments')
