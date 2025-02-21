from django import forms
from .models import Passenger, Train, Tariff, Ticket

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'age', 'gender']

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['train_number', 'train_name']

class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['train', 'price']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['passenger', 'train', 'tariff']