# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
# 渲染主页面
def queryAll(request):
    return render(request, 'index.html')
