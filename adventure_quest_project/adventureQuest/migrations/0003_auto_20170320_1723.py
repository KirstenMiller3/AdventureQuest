# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-20 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventureQuest', '0002_userscores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscores',
            name='score',
            field=models.IntegerField(verbose_name=0),
        ),
    ]
