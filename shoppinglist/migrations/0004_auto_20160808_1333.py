# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0003_auto_20160808_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplelist',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
