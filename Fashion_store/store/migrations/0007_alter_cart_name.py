# Generated by Django 4.1.6 on 2023-02-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart_delete_carts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=122),
        ),
    ]