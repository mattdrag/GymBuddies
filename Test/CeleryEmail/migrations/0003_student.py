# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CeleryEmail', '0002_auto_20150913_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_in_school', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
            ],
        ),
    ]
