from django.db import models

# Create your models here.
from channelaudit.models import CaseProject
from datetime import datetime

class 统计(models.Model):
    project=models.ForeignKey(CaseProject,on_delete=models.CASCADE,verbose_name="项目ID")
    统计_date=models.DateField(default=datetime.date,verbose_name="当天情况")
    刷证_num=models.IntegerField(default=0,verbose_name="刷证数")
    报备_num=models.IntegerField(default=0,verbose_name="报备数")
    可疑渠道_num=models.IntegerField(default=0,verbose_name="可疑数")
    到访识别率=models.FloatField(default=0,verbose_name="到访识别率")

    class Meta:
        unique_together=("project","统计_date")
        verbose_name="统计"
        verbose_name_plural=verbose_name