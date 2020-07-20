from django.db import models


# Create your models here.
# 帖子分类模型
class Category(models.Model):
    cname = models.CharField(max_length=50, unique=True, verbose_name=u'类别名称')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = u'类别'

    def __str__(self):
        return u'Category:%s' % self.cname


# 帖子标签模型
class Tag(models.Model):
    tname = models.CharField(max_length=50, unique=True, verbose_name=u'标签名称')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'

    def __str__(self):
        return u'Tag:%s' % self.tname


# 帖子模型
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'

    def __str__(self):
        return u'Post:%s' % self.title
