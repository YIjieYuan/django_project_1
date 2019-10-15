#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 18:29
# @Author  : Yijie Yuan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_index, name='index'),
    path('<int:note_id>/', views.notes_detail, name='detail'),

]