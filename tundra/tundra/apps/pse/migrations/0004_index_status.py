# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pse', '0003_auto_20160408_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='status',
            field=models.CharField(default='OPEN', max_length=10),
        ),
    ]
