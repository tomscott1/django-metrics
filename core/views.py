# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user(request):
    # define a variable in the views
    user_name = 'Bill'
    return render(request, 'user.html', { 'user_name': user_name })


def metrics(request):
    return render(request, 'metrics.html')
