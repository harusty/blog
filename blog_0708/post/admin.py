# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('cname',)


class TagModelAdmin(admin.ModelAdmin):
    list_display = ('tname',)


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Tag, TagModelAdmin)
admin.site.register(Post, PostModelAdmin)
