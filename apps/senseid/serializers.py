import base64
import os
import imghdr
import io
import base64
import binascii
import uuid
from drf_extra_fields.fields import Base64ImageField, Base64FieldMixin
from rest_framework import serializers



from PIL import Image

from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import (
    DateField,
    DateTimeField,
    DictField,
    FileField,
    FloatField,
    ImageField,
    IntegerField,
)
from rest_framework.utils import html




from channelaudit.models import CaseProjectDevice
from common.models import CaseIdentify
from help.util import timestamp_to_time
from django.utils import six
class CaseBase64ImageField(Base64ImageField):
    """
    自定义了命名方式
    """
    def to_internal_value(self, base64_data):
        # Check if this is a base64 string
        if base64_data in self.EMPTY_VALUES:
            return None

        if isinstance(base64_data, six.string_types):
            # Strip base64 header.
            if ';base64,' in base64_data:
                header, base64_data = base64_data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(base64_data)
            except (TypeError, binascii.Error, ValueError):
                raise ValidationError(self.INVALID_FILE_MESSAGE)
            # Generate file name:
            name=self.context["request"].data["device_id"]+"_"+self.context["request"].data["id_number"]
            # file_name = self.get_file_name()
            file_name=name
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            if file_extension not in self.ALLOWED_TYPES:
                raise ValidationError(self.INVALID_TYPE_MESSAGE)
            complete_file_name = file_name + "." + file_extension
            data = ContentFile(decoded_file, name=complete_file_name)
            return super(Base64FieldMixin, self).to_internal_value(data)
        raise ValidationError(_('Invalid type. This is not an base64 string: {}'.format(
            type(base64_data))))

    # def to_internal_value(self, data):
    #     try:
    #         # `UploadedFile` objects should have name and size attributes.
    #         file_name = data.name
    #         file_size = data.size
    #     except AttributeError:
    #         self.fail('invalid')
    #
    #     if not file_name:
    #         self.fail('no_name')
    #     if not self.allow_empty_file and not file_size:
    #         self.fail('empty')
    #     if self.max_length and len(file_name) > self.max_length:
    #         self.fail('max_length', max_length=self.max_length, length=len(file_name))
    #
    #     return data

class CaseIdentitySerializer(serializers.ModelSerializer):
    id_image=CaseBase64ImageField()
    face_image=CaseBase64ImageField()
    verify_time=serializers.CharField()
    class Meta:
        model = CaseIdentify
        # fields = "__all__"
        exclude = ('project',)

    def validate(self, attrs):
        device_id=attrs["device_id"]
        project=CaseProjectDevice.objects.get(device_id=device_id).project
        attrs["project"]=project

        return attrs


    def validate_verify_time(self, data:str):
        if int(data)>3000000000:
            return str(int(data)//1000)
        else:
            return data
    # def validate_id_image(self,value):
    #     with open(, "rb") as f:
    #
    #     base64_data = base64.b64encode(f.read())
    #     # base64.b64decode(base64data)
    #     print(base64_data)

