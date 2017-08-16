# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import online_shop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop_products', '0003_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='prodcut',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=online_shop_products.models.image_upload_to),
        ),
    ]
