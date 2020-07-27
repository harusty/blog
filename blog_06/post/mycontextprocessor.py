# coding=utf-8
from django.db.models import Count

from post.models import Post


def getCategory(request):
    # 获取分类信息 根据 count的降序排序
    categoryList = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    # 近期文章
    recentBlogs = Post.objects.all().order_by('-created')[:3]

    return {'category_list': categoryList, 'recent_blog': recentBlogs}
