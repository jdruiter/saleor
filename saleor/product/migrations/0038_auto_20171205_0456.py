# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20171129_1004'),
    ]

    operations = [
        migrations.RenameField(model_name='category', old_name='hidden', new_name='is_hidden'),
    ]