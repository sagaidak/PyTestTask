# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160421_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'static/news/pics/no-img.jpg', upload_to=b'static/news/pics/'),
        ),
    ]
