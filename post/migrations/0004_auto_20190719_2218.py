# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190719_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='delete',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='delete',
            field=models.CharField(default=None, max_length=10),
        ),
    ]