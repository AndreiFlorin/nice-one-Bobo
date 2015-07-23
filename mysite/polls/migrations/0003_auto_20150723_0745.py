# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to=b'')),
                ('media_type', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
