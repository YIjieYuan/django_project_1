#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-05 22:38
# @Author  : Yijie Yuan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
