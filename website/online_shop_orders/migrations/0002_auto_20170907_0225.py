# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 02:25
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usercheckout',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
