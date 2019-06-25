from django.db import models

# Create your models here.
from channelaudit.models import CaseProjectDevice


class SenseID(models.Model):
    device_id = models.CharField(max_length=30,unique=True)
    token = models.TextField(default="None",blank=True)
    token_time = models.CharField(max_length=20,default="0",blank=True)
    project_device=models.ForeignKey(CaseProjectDevice,models.CASCADE,verbose_name="对应设备")
    def __str__(self):
        return self.device_id
    class Meta:
        verbose_name="SenseID_Token"
        verbose_name_plural=verbose_name