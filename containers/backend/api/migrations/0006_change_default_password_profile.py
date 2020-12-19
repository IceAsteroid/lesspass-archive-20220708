# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_password_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="password",
            name="length",
            field=models.IntegerField(default=16),
        ),
        migrations.AlterField(
            model_name="password",
            name="version",
            field=models.IntegerField(default=2),
        ),
    ]
