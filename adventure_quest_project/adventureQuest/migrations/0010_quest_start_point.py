# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventureQuest', '0009_remove_riddle_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='start_point',
            field=models.CharField(default='here', max_length=120),
        ),
    ]
