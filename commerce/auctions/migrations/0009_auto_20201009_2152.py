# Generated by Django 3.1.1 on 2020-10-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20201009_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
