# Generated by Django 3.1.1 on 2020-10-09 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20201009_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, choices=[('Fashion', 'Fashion'), ('Gadgets', 'Gadgets'), ('Clothes', 'Clothes'), ('Shoes', 'Shoes'), ('Food/Medications', 'Food/Medications'), ('Art', 'Art'), ('Skincare', 'Skincare')], default='Fashion', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 9, 19, 54, 170811)),
        ),
    ]
