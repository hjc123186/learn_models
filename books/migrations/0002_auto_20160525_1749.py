# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='webstite',
            new_name='website',
        ),
    ]