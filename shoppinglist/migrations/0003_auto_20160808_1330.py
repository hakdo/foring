# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 13:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0002_auto_20160808_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplelist',
            name='contentjson',
        ),
        migrations.AddField(
            model_name='simplelist',
            name='shareable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='simplelist',
            name='sharedwith',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='simplelist',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 8, 13, 30, 51, 397776, tzinfo=utc)),
        ),
    ]
