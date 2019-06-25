from django.db import models
from datetime import datetime

# Create your models here.
from channelaudit.models import CaseProject


class CaseChannel(models.Model):
    """
    导入报备记录
    """
    project = models.ForeignKey(CaseProject, models.CASCADE, verbose_name="项目ID")
    custom_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="客户姓名")
    customer_id_card = models.CharField(max_length=64, verbose_name="证件号码")
    customer_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="客户电话")
    customer_status = models.CharField(max_length=64, blank=True, null=True, verbose_name="订单状态")
    dynatown = models.CharField(max_length=64, blank=True, null=True, verbose_name="置业顾问")
    agent = models.CharField(max_length=64, blank=True, null=True, verbose_name="经纪人")
    channel_company = models.CharField(max_length=64, blank=True, null=True, verbose_name="渠道身份")
    report_time = models.CharField(max_length=64,verbose_name="报备时间")
    special_report_time = models.CharField(max_length=64, blank=True, null=True,
                                           verbose_name="特殊报备时间，如果/，则为正常客户")
    first_look_time = models.CharField(max_length=64,blank=True, null=True, verbose_name="首次带看时间")
    special_first_look_time = models.CharField(max_length=32, blank=True, null=True, verbose_name="特殊带看时间")
    brush_card_time = models.CharField(max_length=64,blank=True, null=True, verbose_name="刷证时间")
    sign_time = models.DateTimeField(max_length=64,blank=True, null=True, verbose_name="签约时间")
    sign_room_num = models.CharField(max_length=64, blank=True, null=True, verbose_name="签约房号")
    IS_DEL = ((0, "不删除"), (1, "删除"))
    is_del = models.IntegerField(choices=IS_DEL, default=0, verbose_name="是否删除")
    create_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="创建者")
    create_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="创建时间")
    update_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="更新者")
    update_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "稽核列表"
        verbose_name_plural = verbose_name
        unique_together = (('project', 'customer_id_card'),)


class CaseIdentify(models.Model):
    """
    刷证记录
    """
    project = models.ForeignKey(CaseProject,models.CASCADE,null=True,blank=True,  verbose_name="项目ID")
    device_id = models.CharField(max_length=64, blank=True, null=True, verbose_name="设备ID")
    CARD_TYPE = (("", "身份证"), ("J", "港澳居住证"), ("I", "外国人永久居住证"))
    card_type = models.CharField(choices=CARD_TYPE, max_length=3, blank=True, null=True,
                                 verbose_name="证件类型，身份证为空，港澳居住证:J，外国人永久居住证：I")
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name="姓名")
    GENDER = ((0, "男"), (1, "女"))
    gender = models.IntegerField(choices=GENDER, blank=True, null=True, verbose_name="性别")
    nation = models.CharField(max_length=64, blank=True, null=True, verbose_name="民族(身份证专有)")
    birthday = models.CharField(max_length=64, blank=True, null=True, verbose_name="出生年月")
    address = models.CharField(max_length=512, blank=True, null=True, verbose_name="住址信息")
    id_number = models.CharField(max_length=64, blank=True, null=True, verbose_name="证件号码")
    authority = models.CharField(max_length=64, blank=True, null=True, verbose_name="签发机关")
    validity = models.CharField(max_length=64, blank=True, null=True, verbose_name="有效期")
    visa_times = models.CharField(max_length=64, blank=True, null=True, verbose_name="签发次数(港澳台)")
    pass_num = models.CharField(max_length=64, blank=True, null=True, verbose_name="通行证号(港澳台)")
    en_name = models.CharField(max_length=64, blank=True, null=True, verbose_name="英文名(外国人)")
    country = models.CharField(max_length=64, blank=True, null=True, verbose_name="国家名(外国人)")
    country_code = models.CharField(max_length=64, blank=True, null=True, verbose_name="国家代码(外国人)")
    dept_code = models.CharField(max_length=64, blank=True, null=True, verbose_name="签发机构代码(外国人)")
    id_image = models.ImageField(upload_to="IdImage", blank=True, null=True, verbose_name="身份证")
    id_image_url = models.URLField(blank=True, null=True, verbose_name="身份证图片URL")
    face_image = models.ImageField(upload_to="FaceImage", blank=True, null=True, verbose_name="现场拍摄人脸")
    face_image_url = models.URLField(blank=True, null=True, verbose_name="现场抓拍图URL")
    verify_time = models.CharField(max_length=15,blank=True, null=True, verbose_name="认证时间")
    RESULT = ((0, "成功"), (1, "失败"), (2, "真人检测失败"), (4, "指纹校验失败"), (5, "OCR校验失败"))
    verify_result = models.IntegerField(choices=RESULT, default=0, verbose_name="认证结果")
    verify_score = models.FloatField(blank=True, null=True, verbose_name="比对分值")
    IS_UPLOAD = ((0, "正常上传"), (1, "数据补传"))
    is_reissue_upload = models.IntegerField(choices=IS_UPLOAD, blank=True, null=True, verbose_name="是否补传")
    IS_DEL = ((0, "不删除"), (1, "删除"))
    is_del = models.IntegerField(choices=IS_DEL, default=0, verbose_name="是否删除")
    create_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="创建者")
    create_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="创建时间")
    update_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="更新者")
    update_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "刷证记录"
        verbose_name_plural = verbose_name
        unique_together = (('project', 'id_number'),)


class CaseIdentifyConfidence(models.Model):
    """
    到访记录
    """
    project = models.ForeignKey(CaseProject, models.CASCADE,null=True,blank=True, verbose_name="项目ID")
    identity = models.ForeignKey(CaseIdentify, models.CASCADE, blank=True, null=True, verbose_name="身份信息ID")
    id_number = models.CharField(max_length=64, blank=True, null=True, verbose_name="身份证号码")
    CONFIDENCE = (("high", "高"), ("medium", "中"), ("low", "低"))
    confidence = models.CharField(choices=CONFIDENCE, max_length=10, blank=True, null=True, verbose_name="匹配度")
    first_snap_time = models.CharField(max_length=15,blank=True, null=True, verbose_name="首次抓拍时间")
    second_snap_time = models.CharField(max_length=15,blank=True, null=True, verbose_name="获取报备时间之前(第一个时间)")
    next_first_snap_time = models.CharField(max_length=15,blank=True, null=True, verbose_name="获取到报备时间后(首次抓拍时间)")
    CUSTOMER_TYPE = ((1, "疑似飞单"), (2, "疑似截客"), (3, "未刷证"), (4, "未报备"), (5, "正常客户"), (6, "确认风险"), (7, "确认正常"), (8, "漏拍"))
    customer_type = models.IntegerField(choices=CUSTOMER_TYPE, default=4, verbose_name="客户类型")
    IS_DEL = ((0, "不删除"), (1, "删除"))
    is_del = models.IntegerField(choices=IS_DEL, blank=True, null=True, verbose_name="是否删除0:不删除，1：删除")
    create_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="创建者")
    create_time = models.DateTimeField(blank=True, null=True, verbose_name="创建时间")
    update_by = models.CharField(max_length=64, blank=True, null=True, verbose_name="更新者")
    update_time = models.DateTimeField(blank=True, null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "到访记录"
        verbose_name_plural = verbose_name
        unique_together = (("project", 'id_number', 'confidence'),)
