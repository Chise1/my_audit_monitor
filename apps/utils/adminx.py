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
from .models import SensetimeID


class SensetimeIDAdmin(object):
    list_display=("name","ak","sk")


xadmin.site.register(SensetimeID, SensetimeIDAdmin)