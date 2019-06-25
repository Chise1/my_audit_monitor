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
from .models import CaseProject, CaseProjectDevice


class CaseProjectAdmin(object):
    list_display = ("sensetimeId", "node", "project_name", "group_id")


class CaseProjectDeviceAdmin(object):
    list_display = ("project", "device_id", "device_type", "device_status")


xadmin.site.register(CaseProject, CaseProjectAdmin)
xadmin.site.register(CaseProjectDevice, CaseProjectDeviceAdmin)
