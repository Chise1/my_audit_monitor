import time
import traceback

from rest_framework import serializers
import xlrd
from common.models import CaseChannel


class ReadModelSerializer(serializers.ModelSerializer):
    xl = serializers.FileField()
    class Meta:
        model = CaseChannel
        fields = ("xl","project")
        # exculde=("")

