# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
            preserve_default=False,
        ),
    ]
