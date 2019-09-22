# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-19 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('face_encoding', models.CharField(max_length=500)),
                ('image_url', models.CharField(max_length=500)),
            ],
        ),
    ]
