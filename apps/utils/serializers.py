from rest_framework import serializers

from utils.models import SensetimeID


class SensetimeIDSerializer(serializers.ModelSerializer):
    class Meta:
        model=SensetimeID
        fields="__all__"