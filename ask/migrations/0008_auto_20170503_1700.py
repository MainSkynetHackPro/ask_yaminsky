# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-03 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0007_auto_20170411_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True, verbose_name='Email'),
        ),
    ]