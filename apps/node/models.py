from django.db import models
from datetime import datetime


# Create your models here.
class CaseNode(models.Model):
    """
    节点管理
    """
    parent_id = models.ForeignKey("self", models.CASCADE, related_name='subs', blank=True, null=True,
                                  verbose_name="父节点")
    parent_ids = models.CharField(max_length=128, blank=True, null=True, verbose_name="父节点集合")
    node_path_name = models.CharField(max_length=512, blank=True, null=True, verbose_name="节点路径名称")
    node_name = models.CharField(max_length=64, verbose_name="节点名称")
    NODE_TYPE = (("M", "集团"), ("F", "城市"), ("C", "区域"), ("X", "项目"))
    node_type = models.CharField(choices=NODE_TYPE, max_length=1, blank=True, null=True,
                                 verbose_name="节点类型（M集团 C区域 F城市）")
    NODE_STATUS = ((1, "启用"), (2, "禁用"))
    node_status = models.IntegerField(choices=NODE_STATUS, default=1, verbose_name="状态")
    node_level = models.IntegerField(blank=True, null=True, verbose_name="资源的级数，树状结构")
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name="节点图标")
    sort = models.IntegerField(blank=True, null=True, verbose_name="排序")
    EXIST_AVERT_FUNCTION = ((0, "存在规则"), (1, "没有规则"))
    exists_avert_function = models.IntegerField(choices=EXIST_AVERT_FUNCTION, blank=True, null=True, default=1,
                                                verbose_name="是否有稽核规则")
    AVERT_FLY = ((1, "报备时间"), (2, "首次带看时间"))
    avert_fly_sheet_audit_time = models.IntegerField(choices=AVERT_FLY, blank=True, null=True, verbose_name="防飞单稽核时间")
    fly_sheet_audit_tolerance = models.IntegerField(default=30, verbose_name="稽核时间容差，单位min")
    AVERT_STATUS = (("on", "开启"), ("off", "关闭"))
    avert_carrying_capacity_status = models.CharField(choices=AVERT_STATUS, default="off", max_length=4, blank=True,
                                                      null=True,
                                                      verbose_name="防载客功能状态")
    avert_carrying_capacity_tolerance = models.IntegerField(default=30, verbose_name="防载客时间容差，单位min")
    customer_protect_time = models.IntegerField(blank=True, null=True, verbose_name="客户保护时长（天）")

    IS_DEL = ((0, "不删除"), (1, "删除"))
    is_del = models.IntegerField(choices=IS_DEL, default=0, verbose_name="是否删除")
    create_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="创建者")
    create_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="创建时间")
    update_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="更新者")
    update_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "节点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%d %s" % (self.id, self.node_name)
