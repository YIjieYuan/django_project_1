#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:38
# @Author  : Yijie Yuan
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    return HttpResponse('Welcome by yuanyijie!')
