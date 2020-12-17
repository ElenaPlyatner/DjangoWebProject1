# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-16 13:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201216_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 16, 16, 38, 49, 892717), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 16, 16, 38, 49, 894718), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 16, 16, 38, 49, 895720), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Products', verbose_name='Товар'),
        ),
    ]
