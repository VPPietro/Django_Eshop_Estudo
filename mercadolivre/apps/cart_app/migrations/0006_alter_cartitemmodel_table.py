# Generated by Django 3.2.4 on 2021-09-07 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0005_alter_cartitemmodel_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cartitemmodel',
            table='cart_item',
        ),
    ]