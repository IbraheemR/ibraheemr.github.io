# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171119_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='extra_content',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]