# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20160421_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'news/pics/no-img.jpg', upload_to=b'news/pics/'),
        ),
    ]