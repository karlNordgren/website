# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Location')),
                ('Album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Album')),
            ],
        ),
    ]
