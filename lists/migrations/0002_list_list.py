# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2023-04-26 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
