from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_passenger/', views.add_passenger, name='add_passenger'),
    path('view_passengers/', views.view_passengers, name='view_passengers'),
    path('add_train/', views.add_train, name='add_train'),
    path('view_trains/', views.view_trains, name='view_trains'),
    path('add_tariff/', views.add_tariff, name='add_tariff'),
    path('view_tariffs/', views.view_tariffs, name='view_tariffs'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),
    path('view_tickets/', views.view_tickets, name='view_tickets'),
]