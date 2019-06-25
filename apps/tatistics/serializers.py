
from rest_framework import serializers

from tatistics.models import 统计


class 统计Serializer(serializers.ModelSerializer):

    class Meta:
        model=统计
        fields=("project","统计_date")