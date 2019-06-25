import base64
import json

from django.http import HttpResponse
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from channelaudit.models import CaseProject
from help.访问sensego2 import sensego_multiidentify
from .serializers import *


# Create your views here.
class FaceSearchViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = FaceSearchSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = CaseProject.objects.get(id=int(request.data['project']))
        sensetime = project.sensetimeId
        ak = sensetime.ak
        sk = sensetime.sk
        group_id = project.group_id
        face_image = base64.b64encode(request.data["image"].read())
        # with open("face.txt","w") as f:
        #     f.write(face_image)
        pxxx = sensego_multiidentify(ak, sk, group_id, face_image)
        print(pxxx)
        # data =pxxx["results"][0]['arrived_at']
        # print(data)
        # request.data["first_look"]=data

        return Response(pxxx )
        # return JsonResponse(data=re,status=status.HTTP_201_CREATED,headers=headers)

def faces_searchs(request):
    # request.user.has_perms()
    print(request.user)
    if request.method =="POST":
        a=request.POST["a"]
        b=request.POST["b"]
        re={"code":"0"}
        print(True)
        return HttpResponse(json.dumps(re))
        # return Response(json.dumps(re), status=status.HTTP_201_CREATED)