# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar'),
        ),
    ]
