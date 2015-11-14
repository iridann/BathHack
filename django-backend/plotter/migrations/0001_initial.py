# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('creation_date', models.DateField(verbose_name='Measurement Date')),
                ('creation_time', models.TimeField(verbose_name='Measurement Time')),
                ('value', models.FloatField()),
            ],
        ),
    ]
