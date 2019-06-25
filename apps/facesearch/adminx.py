#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from .models import FaceSearch


class FaceSearchAdmin(object):
    # list显示的数据
    list_display = ('project', 'image')
    # 每页多少个
    list_per_page = 20
    # 搜索
    # search_fields = ("project",)
    # 字段过滤
    list_filter = ('project__project_name',)


xadmin.site.register(FaceSearch, FaceSearchAdmin)
