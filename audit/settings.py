"""
Django settings for audit project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import threadpool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 调整apps等的地址到这里面，设置项目运行path。
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's--oayn02v8+#@4^hd8@)g27qq0w@6l)dgd&l7mqd)&o-fila-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    # xadmin注册
    'xadmin',
    'crispy_forms',
    'django.contrib.admin',
    # 富文本编辑器
    'DjangoUeditor',
    'rest_framework',
    # 注册
    'django_filters',
    # 跨域配置
    'corsheaders',
    # 配置token登录
    'rest_framework.authtoken',
    # 注册app
    'facesearch',
    'common',
    'channelaudit',
    'node',
    'utils',
    'senseid',
    'excel_read',
    'tatistics',
]
MIDDLEWARE = [
    # 配置跨域
    'corsheaders.middleware.CorsMiddleware',  # 最好添加至第一行
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'audit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'audit.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "audit_python",
        # 从源数据库反向生成
        # 'NAME': "audit",
        "USER": "root",
        "PASSWORD": "mnbvcxz123",
        "HOST": "127.0.0.1",
        # "HOST": "180.76.60.166",
        # "OPTIONS": {"init_command": "SET default_storage_engine=INNODB;"}  # 不使用mysql默认引擎，使用INNODB引擎，配合之后的第三方登录
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "static"
# redis缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# jwt配置
import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_HEADER_PREFIX': '',
}
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    # 　注：'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'适用于添加身份验证和权限。
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # 'rest_framework.permissions.IsAuthenticated',#??

    # ],
    # 设置api速度限制，防止爬虫影响系统效率
    'DEFAULT_THROTTLE_CLASS': (
        # 匿名用户
        'rest_framework.throttling.AnonRateThrottle',
        # 登录用户
        'rest_framework.throttling.UserRateThrottle'
    ),
    # 访问次数限制
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/second',
        'user': '3/second'
    },

    # 配置分页,也可以创建页类实例进行分页功能
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #     'PAGE_SIZE': 10,
    # 配置字段过滤搜索
    # 配置auth登录权限方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',  # 使用token验证，全局验证，针对所有访问
        # 使用JWT方式验证登录
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',  # 需要验证的时候通过账户密码验证。
        'rest_framework.authentication.SessionAuthentication',  # 使用session验证
    )
}

# 设置图片访问
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media').replace('\\', '/'),
)

# senseid的salt
salt = "#bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8"
# 服务器版本号
service_version = "1.0.0"
#导入线程池
from multiprocessing.pool import ThreadPool
pool=ThreadPool(32)