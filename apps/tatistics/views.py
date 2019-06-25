from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, viewsets, status

from tatistics.serializers import 统计Serializer


# class 统计Viewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
#     serializer_class = 统计Serializer
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
