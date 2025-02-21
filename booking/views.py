from django.shortcuts import render, redirect
from .models import Passenger, Train, Tariff, Ticket
from .forms import PassengerForm, TrainForm, TariffForm, TicketForm

def dashboard(request):
    return render(request, 'booking/dashboard.html')

def add_passenger(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_passengers')
    else:
        form = PassengerForm()
    return render(request, 'booking/add_passenger.html', {'form': form})

def view_passengers(request):
    passengers = Passenger.objects.all()
    return render(request, 'booking/view_passengers.html', {'passengers': passengers})

def add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_trains')
    else:
        form = TrainForm()
    return render(request, 'booking/add_train.html', {'form': form})

def view_trains(request):
    trains = Train.objects.all()
    return render(request, 'booking/view_trains.html', {'trains': trains})

def add_tariff(request):
    if request.method == 'POST':
        form = TariffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_tariffs')
    else:
        form = TariffForm()
    return render(request, 'booking/add_tariff.html', {'form': form})

def view_tariffs(request):
    tariffs = Tariff.objects.all()
    return render(request, 'booking/view_tariffs.html', {'tariffs': tariffs})

def book_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_tickets')
    else:
        form = TicketForm()
    return render(request, 'booking/book_ticket.html', {'form': form})

def view_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'booking/view_tickets.html', {'tickets': tickets})