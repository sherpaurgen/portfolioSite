# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180616_0642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='showcase3',
            new_name='showcaseimage1',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='showcase1',
            new_name='showcaseimage2',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='showcase2',
            new_name='showcaseimage3',
        ),
    ]