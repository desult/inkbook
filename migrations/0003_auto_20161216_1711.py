# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-16 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inkbook', '0002_series_specs_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inkcolor',
            name='opacity',
        ),
        migrations.AddField(
            model_name='inkcolor',
            name='series',
            field=models.ForeignKey(default='480', on_delete=django.db.models.deletion.CASCADE, to='inkbook.Series'),
            preserve_default=False,
        ),
    ]
