# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_auto_20170614_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.Usuario'),
        ),
    ]
