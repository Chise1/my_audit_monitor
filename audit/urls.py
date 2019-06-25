"""audit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
from django.urls import NoReverseMatch, reverse
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
import xadmin
from audit import settings
from common.views import ConfigureViewset
from django.views.static import serve

from excel_read.views import ReadModelViewset
from facesearch.views import FaceSearchViewset, faces_searchs
from senseid.views import HeartbeatView, AuthView, UploadView
from utils.views import *

router = DefaultRouter()
# router.register(r'api/common/configure/data',ConfigureViewset.as_view())
router.register(r'facesearchs', FaceSearchViewset, base_name="人脸搜索")
# router.register(r'senseid/auth',AuthViewset,base_name="鉴权")
# router.register(r'senseid/upload_data_full',UploadView,base_name="鉴权")
senseid_router = DefaultRouter()
senseid_router.register(r'upload_data_full', UploadView, base_name="上传测试")
# senseid_router.register(r'auth',AuthView,base_name="鉴权")
router.register(r'readmodel',ReadModelViewset,base_name="导入测试")
urlpatterns = [
    path(r'admin/', xadmin.site.urls),
    path(r'login', obtain_jwt_token),
    # 返回版本号
    path(r'api/common/configure/data', ConfigureViewset.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'senseid', include(router.urls)),
    path(r'senseid/heartbeat', HeartbeatView.as_view(),),
    path(r'senseid/auth', AuthView.as_view(), ),
    re_path(r'senseid/', include(senseid_router.urls)),
    re_path(r'', include(router.urls)),

    path(r'faces_searchs', faces_searchs),

    # path(r'senseid/upload_data_full',UploadView.as_view(),)
]
