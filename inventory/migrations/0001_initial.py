# Generated by Django 5.0.3 on 2024-03-10 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('category', models.CharField(choices=[('medical supplies', 'medical supplies'), ('medical equipment', 'medical equipment'), ('medications', 'medications')], max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_available', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('product_in', models.IntegerField(blank=True, null=True)),
                ('opening_numbers_of_product', models.IntegerField(blank=True, null=True)),
                ('closing_number_of_products', models.IntegerField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.supplier'),
        ),
    ]
