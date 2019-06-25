from django.db import models
from datetime import datetime

# Create your models here.
from node.models import CaseNode
from utils.models import SensetimeID


class CaseProject(models.Model):
    sensetimeId = models.ForeignKey(SensetimeID, models.CASCADE, verbose_name="商汤秘钥", related_name="SENSETIMEID")
    node = models.ForeignKey(CaseNode, models.CASCADE, blank=True, null=True, verbose_name="节点ID")
    PROJCET_STATUS = ((1, "启用"), (2, "禁用"))
    project_name = models.CharField(max_length=128, verbose_name="项目名称")
    project_addr = models.CharField(max_length=128, blank=True, null=True, verbose_name="项目地址")
    project_status = models.IntegerField(default=1, verbose_name="项目状态", choices=PROJCET_STATUS)
    group_id = models.CharField(max_length=32, verbose_name="项目GROUP_ID")
    hard_dog_nums = models.CharField(max_length=32, blank=True, null=True, verbose_name="硬狗序列号")
    node_path_id = models.CharField(max_length=64, blank=True, null=True, verbose_name="节点路径ID")
    node_path_name = models.CharField(max_length=256, blank=True, null=True, verbose_name="节点路径名称")
    forward_url = models.CharField(max_length=256, blank=True, null=True, verbose_name="??")
    offline_notice_email = models.CharField(max_length=32, blank=True, null=True, verbose_name="离线告警邮箱")
    offline_notice_mobile = models.CharField(max_length=32, blank=True, null=True,
                                             verbose_name="离线通知手机")
    authorize_url = models.CharField(max_length=512, blank=True, null=True, verbose_name="授权URL")
    valid_date = models.DateTimeField(blank=True, null=True, verbose_name="项目有效期")
    ALLOT_TYPE = ((1, "遵循父节点"), (2, "自定义"))
    allot_user_type = models.IntegerField(choices=ALLOT_TYPE, verbose_name="分配用户类型")
    IS_DEL = ((0, "不删除"), (1, "删除"))
    is_del = models.IntegerField(choices=IS_DEL,default=0, verbose_name="是否删除")
    create_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="创建者")
    create_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="创建时间")
    update_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="更新者")
    update_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "项目列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_name


class CaseProjectDevice(models.Model):
    project = models.ForeignKey(CaseProject, models.CASCADE, blank=True, null=True)
    device_id = models.CharField(max_length=128,unique=True, blank=True, null=True, verbose_name="设备ID")
    device_name = models.CharField(max_length=128, verbose_name="设备名称")
    DEVICE_TYPE = ((1, "一体机"), (2, "摄像头"), (3, "前端服务器"))
    device_type = models.IntegerField(choices=DEVICE_TYPE, blank=True, null=True, verbose_name="设备类型")
    DEVICE_STATUS = ((0, "正常"), (1, "离线"))
    device_status = models.IntegerField(choices=DEVICE_STATUS, blank=True, null=True, verbose_name="设备状态")
    IS_DEL = ((0, "不删除"), (1, "删除"))
    is_del = models.IntegerField(choices=IS_DEL,default=0, verbose_name="是否删除")
    create_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="创建者")
    create_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="创建时间")
    update_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="更新者")
    update_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "设备列表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.device_name
