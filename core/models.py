# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# create timestamped base class
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'users'


class Metric(TimeStampedModel):
    name = models.CharField(max_length=128, null=False)
    is_bool = models.BooleanField(blank=False)
    max_val = models.IntegerField(null=True)
    min_val = models.IntegerField(null=True)
    increment = models.IntegerField(null=True)
    # slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'metrics'


class Record(TimeStampedModel):
    value = models.IntegerField(null=False)
    date = models.DateField(null=False)

    class Meta:
        db_table = 'records'
