# Generated by Django 2.1.7 on 2019-09-06 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]