#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:38
# @Author  : Yijie Yuan
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def index(request):
    print('hi')
    # return render(request, 'mysite/index.html', )
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        message = '请检查填写的内容！'
        if username.strip() and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                message = '账号未激活'
                if user.is_active:
                    auth.login(request, user)
                    print(1)
                    return redirect('.')

                else:
                    print(2)
                    return render(request, 'mysite/index.html', {'message': message})

            else:
                message = '账号密码输入错误！'
                print(3)
                return render(request, 'mysite/index.html', {'message': message})


            # 还可以,
            # 用户名字符合法性验证
            # 密码长度验证...
        else:
            print(4)
            return render(request, 'mysite/index.html', {'message': message})
    print(5)
    return render(request, 'mysite/index.html', {'message': message})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


