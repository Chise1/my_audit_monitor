from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from facesearch.models import FaceSearch


class FaceSearchSerializer(serializers.ModelSerializer):
    first_look=serializers.DateTimeField()
    class Meta:
        model = FaceSearch
        fields = ("image","project","first_look")