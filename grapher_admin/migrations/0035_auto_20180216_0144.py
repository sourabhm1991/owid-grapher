# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-16 01:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grapher_admin', '0034_auto_20180216_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='displayIsProjection',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='displayName',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='displayNumDecimalPlaces',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='displayShortUnit',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='displayTolerance',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='displayUnit',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='displayUnitConversionFactor',
        ),
    ]
