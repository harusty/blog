# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.paginator import Paginator

# Create your views here.
# 渲染主页面
from post.models import Post


def queryAll(request, num=1):
    # 获取当前页面
    num = int(num)

    # 获取所有的帖子
    postList = Post.objects.all().order_by('-created')

    # 创建分页器对象 ,每页显示一条
    pageObj = Paginator(postList, 1)

    # 获取当前页的数据
    perPageList = pageObj.page(num)

    # 生成页码数列表
    # 每页开始页码
    import math
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)

    print(pageList)

    return render(request, 'index.html', {'postList': perPageList, 'pageList': pageList, 'currentNum': num})


def postDetail(request, postId):
    postId = int(postId)
    # 根据postId 获取 帖子详情信息
    postObjItem = Post.objects.get(id=postId)
    return render(request, 'post_detail.html', {'post': postObjItem})


# 根据发帖时间查询所有帖子
def queryPostByCreated(request, year, month):
    postList = Post.objects.filter(created__year=year, created__month=month)
    return render(request, 'article.html', {'postList': postList})


# 根据类别id查询所有帖子
def queryPostByCid(request, cid):
    postList = Post.objects.filter(category_id=cid)
    # Post.objects.filter(category__id=cid)
    return render(request, 'article.html', {'postList': postList})
