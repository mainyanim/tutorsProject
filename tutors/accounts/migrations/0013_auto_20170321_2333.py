# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20170321_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(default='Hello World!', max_length=100),
        ),
    ]