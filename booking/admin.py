from django.contrib import admin

from .models import Passenger, Train, Tariff, Ticket

admin.site.register(Passenger)
admin.site.register(Train)
admin.site.register(Tariff)
admin.site.register(Ticket)
