# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-16 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201216_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 16, 16, 36, 16, 531262), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 16, 16, 36, 16, 532262), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 16, 16, 36, 16, 534264), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Цена'),
        ),
    ]
