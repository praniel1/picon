# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='person',
        ),
    ]
