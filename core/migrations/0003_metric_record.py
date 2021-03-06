# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170830_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('is_bool', models.BooleanField()),
                ('max_val', models.IntegerField(null=True)),
                ('min_val', models.IntegerField(null=True)),
                ('increment', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'metrics',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
