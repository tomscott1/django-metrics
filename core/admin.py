# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from core.models import User, Metric, Record

admin.site.register(User)
admin.site.register(Metric)
admin.site.register(Record)


# # set up automated slug creation
# class ThingAdmin(admin.ModelAdmin):
#     model = Thing
#     list_display = ('name', 'description',)
#     prepopulated_fields = {'slug': ('name',)}

# admin.site.register(Thing, ThingAdmin)
