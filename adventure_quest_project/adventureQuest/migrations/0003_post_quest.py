# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-16 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventureQuest', '0002_comment_post_quest_riddle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adventureQuest.Quest'),
        ),
    ]