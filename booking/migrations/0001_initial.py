# Generated by Django 5.1.6 on 2025-02-21 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.CharField(max_length=20)),
                ('train_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.passenger')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.tariff')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.train')),
            ],
        ),
        migrations.AddField(
            model_name='tariff',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.train'),
        ),
    ]
