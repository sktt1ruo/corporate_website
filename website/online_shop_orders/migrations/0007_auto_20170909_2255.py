# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop_orders', '0006_auto_20170909_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]