# coding=utf-8
from django.db.models import Count

from post.models import Post


def getCategory(request):
    # 获取分类信息 根据 count的降序排序
    categoryList = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    # 近期文章
    recentBlogs = Post.objects.all().order_by('-created')[:3]

    # 获取归档数据，根据日期进行归档
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select created,count('*') from t_post GROUP BY DATE_FORMAT(created,'%Y-%m');")
    guidangBlogs = cursor.fetchall()

    return {'category_list': categoryList, 'recent_blog': recentBlogs, 'guidang_blog': guidangBlogs}
