# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='creation_time',
        ),
        migrations.AddField(
            model_name='measurement',
            name='creation_dt',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 14, 14, 54, 45, 966847, tzinfo=utc), verbose_name='Creation DateTime'),
            preserve_default=False,
        ),
    ]
