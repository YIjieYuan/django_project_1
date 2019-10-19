#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 18:29
# @Author  : Yijie Yuan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path, reverse
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_index, name='index'),
    # path('<int:note_id>/', views.notes_detail, name='detail'),
    re_path(r'^(?P<category>[\w\-]+)/$', views.notes_list, name='list'),
    re_path(r'^(?P<category>[\w\-]+)/(?P<notes_slug>[\w\-]+)/$', views.notes_detail, name='detail'),

]