# Generated by Django 4.1.6 on 2023-02-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
