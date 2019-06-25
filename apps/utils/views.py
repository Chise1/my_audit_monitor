from django.shortcuts import render

# Create your views here.


import json
import threading
import requests
from django.http import HttpResponse
import copy
# Create your views here.
from django.shortcuts import render
from rest_framework import mixins, viewsets, status

# def test(request):
#     print("http:",request.META["PATH_INFO"])
#     return HttpResponse(json.dumps(heartbeat_true), content_type='application/json')
from rest_framework.response import Response


# class AuthViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
#     """
#     鉴权方法
#     """
#     pass
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
# def auth_views(request):
#
#     if request.method == "GET":
#         HttpResponse(json.dumps(auth_false_402("误用GET请求")), content_type='application/json')
#     else:
#         if not senseid.全局变量.token_safe:
#             print("token_safe")
#             senseid.全局变量.token_safe = True
#             threading.Thread(target=get_token).start()
#         post_value = request.POST
#         print("auth:", post_value)
#         # sign=get_sign(post_value.device_id,int(time.time()),post_value.version)
#         threading.Thread(target=forward_auth, args=(post_value,)).start()
#         senseid_version[post_value["device_id"]] = post_value["version"]
#         if auth_callback(post_value):
#             re = json.dumps(auth_true(get_token2(post_value)))
#             return HttpResponse(re, content_type='application/json')
#         else:
#             re = json.dumps(auth_false_401)
#             return HttpResponse(re, content_type='application/json')
#
#
# def heartbeat_views(request):
#     if request.method == "GET":
#         HttpResponse(json.dumps(heartbeat_false_402("误用GET请求")), content_type='application/json')
#     else:
#         if not senseid.全局变量.token_safe:
#             print("token_safe")
#             senseid.全局变量.token_safe = True
#             threading.Thread(target=get_token).start()
#         post_value = request.POST
#         threading.Thread(target=forward_heartbeat, args=(post_value,)).start()
#         if heartbeat_callback(post_value):
#             re = json.dumps(heartbeat_true)
#             return HttpResponse(re, content_type='application/json')
#         else:
#             raise Exception("sign验证错误")
#
#
# def upload_views(request):
#     print("upload_data_full_views")
#     print("true")
#     if not senseid.全局变量.token_safe:
#         print("token_safe")
#         senseid.全局变量.token_safe = True
#         threading.Thread(target=get_token).start()
#     if request.method == "GET":
#         HttpResponse(json.dumps(upload_data_false_402("误用GET请求")), content_type='application/json')
#     else:
#         model = request.POST  # 数据
#         print("model:", model)
#         if model is not None:
#             # 保存数据
#             threading.Thread(target=save_sid, args=(model,)).start()
#             # 上传数据返回的值
#             threading.Thread(target=forward_upload, args=(model,)).start()
#             person = Person(
#                             device_id=model['device_id'],
#                             card_type=model['card_type'],
#                             name=model['name'],
#                             sex=str(model['sex']),
#                             nation=model['nation'],
#                             birthday=model['birthday'],
#                           )
#             person.save()
#             print("asdfasdf")
#             return HttpResponse(json.dumps(upload_data_true), content_type='application/json')
#             # if test_token(model):
#             #     upload_return = upload_data_true
#             #     print("true")
#             #     return HttpResponse(json.dumps(upload_return), content_type='application/json')
#             # else:
#             #     print("false")
#             #     # upload_return = upload_data_false_401
#             #     upload_return = upload_data_true
#             #     return HttpResponse(json.dumps(upload_return), content_type='application/json')
#         else:
#             upload_return = upload_data_true
#             time.sleep(5)
#             # return HttpResponse(json.dumps(upload_return), content_type='application/json')
#
#
# def forward_upload(data, url0=None, **kwargs):
#     if url0 == None:
#         uploads = SenseIDURL.objects.filter(device_id=data["device_id"]).values('url')
#         for k in uploads:
#             data0 = dict(copy.deepcopy(data))
#             threading.Thread(target=forward_upload, args=(data0, k["url"])).start()
#         return True
#     else:
#         if url0[-1] == r"/":
#             url1 = url0 + "upload_data_full"
#         else:
#             url1 = url0 + "/upload_data_full"
#         print(url0)
#         try:
#             senseid = SenseIDURL.objects.get(url=url0)
#             data["token"] = senseid.token
#             print(url1)
#             r = requests.post(url1, data=data)
#             rs = r.json()
#             upload_control_callback(url0, rs, data)
#             return None
#         except:
#             print(url0)
#
#
# def forward_auth(data, url0=None):
#     if url0 == None:
#         device_id = data["device_id"]
#         urls = SenseIDURL.objects.filter(device_id=device_id).values('url')
#         for url in urls:
#             threading.Thread(target=forward_auth, args=(data, url["url"])).start()
#         return True
#     else:
#         if url0[-1] == r"/":
#             url1 = url0 + "auth"
#         else:
#             url1 = url0 + "/auth"
#         r = requests.post(url1, data=data)
#         auth_control_callback(url0, r.json())
#         return True
#
#
# def forward_heartbeat(data, url0=None):
#     if url0 == None:
#         device_id = data["device_id"]
#         urls = list(SenseIDURL.objects.filter(device_id=device_id).values('url'))  ##修改了
#         for k in urls:
#             threading.Thread(target=forward_heartbeat, args=(data, k["url"])).start()
#         return True
#     else:
#         if url0[-1] == r"/":
#             url1 = url0 + "heartbeat"
#
#         else:
#             url1 = url0 + "/heartbeat"
#         r = requests.post(url1, data=dict(data))
#         heartbeat_control_callback(url0, r.json())
#         return True
