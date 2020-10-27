# Generated by Django 3.1.1 on 2020-10-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='item_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=255),
        ),
    ]
