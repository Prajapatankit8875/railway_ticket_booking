
from django.db import models

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Train(models.Model):
    train_number = models.CharField(max_length=20)
    train_name = models.CharField(max_length=100)

    def __str__(self):
        return self.train_name

class Tariff(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.train.train_name} - {self.price}"

class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket for {self.passenger.name} on {self.train.train_name}"
