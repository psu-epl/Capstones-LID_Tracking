# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0003_auto_20170327_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='punches',
            name='smid',
        ),
        migrations.AddField(
            model_name='punches',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aum.Tool'),
        ),
    ]
