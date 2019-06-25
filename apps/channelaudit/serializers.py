from rest_framework import serializers

from channelaudit.models import CaseProject
from facesearch.serializers import FaceSearchSerializer
from utils.serializers import SensetimeIDSerializer


class CaseProjectSerializer(serializers.ModelSerializer):
    sensetimeId=SensetimeIDSerializer()
    class Meta:
        model=CaseProject
        fields=("id",)

class CaseProject_Search_Serializer(serializers.ModelSerializer):
    facesearch=FaceSearchSerializer()
    class Meta:
        model=CaseProject
        fields=("project_name","facesearch")