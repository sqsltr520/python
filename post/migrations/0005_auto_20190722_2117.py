# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-22 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190719_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='delete',
            field=models.BooleanField(),
        ),
    ]