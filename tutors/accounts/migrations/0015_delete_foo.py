# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_foo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Foo',
        ),
    ]