# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 01:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171018_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]
