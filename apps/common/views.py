from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, mixins
# 缓存
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
import json


# Create your views here.

class ConfigureViewset(View):

    def post(self, request, *args, **kwargs):
        d = {
            "code": "000",
            "message": "查询成功",
            "data": {
                "website_name": "案场稽核系统管理平台",
                "website_logo": "profile/websiteConfigure\\b0962cff35195decb2333bb4b28ede1b.png",
                "website_cross_domain": "",
                "version": "v1.0.1",
                "website_ico": "profile/websiteConfigure\\2faff6387acbe82da1d02422f6075641.png"
            }
        }
        return HttpResponse(json.dumps(d), content_type="application/json,charset=utf-8")
