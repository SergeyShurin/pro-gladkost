# Generated by Django 2.0.5 on 2018-06-15 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0019_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
    ]
