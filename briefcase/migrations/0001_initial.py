# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('lang_main', models.CharField(max_length=255)),
                ('lang_all', models.TextField()),
                ('image_url', models.CharField(max_length=255)),
                ('port_url', models.CharField(max_length=255)),
                ('site_url', models.CharField(max_length=255)),
                ('github_url', models.CharField(max_length=255)),
                ('importance', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
