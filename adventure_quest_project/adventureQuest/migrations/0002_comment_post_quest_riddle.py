# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-13 14:33
from __future__ import unicode_literals

import adventureQuest.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventureQuest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='heigth_field', null=True, upload_to=adventureQuest.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=120)),
                ('age_limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=128)),
                ('answer', models.CharField(max_length=128)),
                ('quest_name', models.CharField(max_length=128)),
                ('question_id', models.IntegerField(verbose_name=0)),
            ],
        ),
    ]
