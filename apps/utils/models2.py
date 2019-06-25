from django.db import models

# Create your models here.
class CaseNum(models.Model):
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_num'


class Num(models.Model):
    i = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'num'


class OrgnineCaseChannel(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    custom_name = models.CharField(max_length=128, blank=True, null=True)
    customer_id_card = models.CharField(max_length=64, blank=True, null=True)
    customer_phone = models.CharField(max_length=64, blank=True, null=True)
    customer_status = models.CharField(max_length=64, blank=True, null=True)
    customer_type = models.CharField(max_length=64, blank=True, null=True)
    dynatown = models.CharField(max_length=64, blank=True, null=True)
    agent = models.CharField(max_length=64, blank=True, null=True)
    channel_company = models.CharField(max_length=64, blank=True, null=True)
    report_time = models.DateTimeField(blank=True, null=True)
    special_report_time = models.CharField(max_length=64, blank=True, null=True)
    first_snap_time = models.DateTimeField(blank=True, null=True)
    first_look_time = models.DateTimeField(blank=True, null=True)
    special_first_look_time = models.CharField(max_length=32, blank=True, null=True)
    brush_card_time = models.DateTimeField(blank=True, null=True)
    sign_time = models.DateTimeField(blank=True, null=True)
    sign_room_num = models.CharField(max_length=64, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_channel'
        unique_together = (('project_id', 'customer_id_card'),)


class OrgnineCaseIdentity(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    card_type = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    nation = models.CharField(max_length=64, blank=True, null=True)
    birthday = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    id_number = models.CharField(max_length=64, blank=True, null=True)
    authority = models.CharField(max_length=64, blank=True, null=True)
    validity = models.CharField(max_length=64, blank=True, null=True)
    visa_times = models.CharField(max_length=64, blank=True, null=True)
    pass_num = models.CharField(max_length=64, blank=True, null=True)
    en_name = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    country_code = models.CharField(max_length=64, blank=True, null=True)
    dept_code = models.CharField(max_length=64, blank=True, null=True)
    id_image = models.TextField(blank=True, null=True)
    id_image_url = models.CharField(max_length=5000, blank=True, null=True)
    face_image = models.TextField(blank=True, null=True)
    face_image_url = models.CharField(max_length=5000, blank=True, null=True)
    verify_time = models.DateTimeField(blank=True, null=True)
    first_snap_time = models.DateTimeField(blank=True, null=True)
    confidence = models.CharField(max_length=32, blank=True, null=True)
    verify_result = models.IntegerField(blank=True, null=True)
    verify_score = models.FloatField(blank=True, null=True)
    is_reissue_upload = models.CharField(max_length=32, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_identity'
        unique_together = (('project_id', 'id_number'),)


class OrgnineCaseIdentityConfidence(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    identity_id = models.IntegerField(blank=True, null=True)
    id_number = models.CharField(max_length=64, blank=True, null=True)
    confidence = models.CharField(max_length=32, blank=True, null=True)
    first_snap_time = models.DateTimeField(blank=True, null=True)
    second_snap_time = models.DateTimeField(blank=True, null=True)
    next_first_snap_time = models.DateTimeField(blank=True, null=True)
    customer_type = models.CharField(max_length=32, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_identity_confidence'
        unique_together = (('id_number', 'confidence'),)


class OrgnineCaseNode(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    parent_ids = models.CharField(max_length=128, blank=True, null=True)
    node_path_name = models.CharField(max_length=512, blank=True, null=True)
    node_name = models.CharField(max_length=64, blank=True, null=True)
    node_type = models.CharField(max_length=1, blank=True, null=True)
    node_status = models.IntegerField(blank=True, null=True)
    node_level = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    exists_avert_function = models.IntegerField(blank=True, null=True)
    avert_fly_sheet_audit_time = models.CharField(max_length=4, blank=True, null=True)
    fly_sheet_audit_tolerance = models.IntegerField(blank=True, null=True)
    avert_carrying_capacity_status = models.CharField(max_length=4, blank=True, null=True)
    avert_carrying_capacity_tolerance = models.IntegerField(blank=True, null=True)
    customer_protect_time = models.IntegerField(blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_node'


class OrgnineCaseProject(models.Model):
    project_name = models.CharField(max_length=128, blank=True, null=True)
    project_addr = models.CharField(max_length=128, blank=True, null=True)
    project_status = models.CharField(max_length=4, blank=True, null=True)
    camera_nums = models.TextField(blank=True, null=True)
    server_nums = models.TextField(blank=True, null=True)
    integrated_machine_nums = models.TextField(blank=True, null=True)
    group_id = models.CharField(max_length=32, blank=True, null=True)
    hard_dog_nums = models.CharField(max_length=32, blank=True, null=True)
    node_id = models.IntegerField(blank=True, null=True)
    node_path_id = models.CharField(max_length=64, blank=True, null=True)
    node_path_name = models.CharField(max_length=256, blank=True, null=True)
    forward_url = models.CharField(max_length=256, blank=True, null=True)
    avert_fly_sheet_audit_time = models.CharField(max_length=4, blank=True, null=True)
    fly_sheet_audit_tolerance = models.IntegerField(blank=True, null=True)
    avert_carrying_capacity_status = models.CharField(max_length=4, blank=True, null=True)
    avert_carrying_capacity_tolerance = models.IntegerField(blank=True, null=True)
    customer_protect_time = models.IntegerField(blank=True, null=True)
    offline_notice_email = models.CharField(max_length=32, blank=True, null=True)
    offline_notice_mobile = models.CharField(max_length=32, blank=True, null=True)
    authorize_url = models.CharField(max_length=512, blank=True, null=True)
    valid_date = models.DateTimeField(blank=True, null=True)
    allot_user_type = models.CharField(max_length=4, blank=True, null=True)
    user_ids = models.CharField(max_length=128, blank=True, null=True)
    sense_id = models.IntegerField(blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_project'


class OrgnineCaseProjectDevice(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    device_id = models.CharField(max_length=128, blank=True, null=True)
    device_name = models.CharField(max_length=128, blank=True, null=True)
    device_type = models.CharField(max_length=4, blank=True, null=True)
    device_status = models.CharField(max_length=4, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_project_device'
        unique_together = (('project_id', 'device_id', 'device_type'),)


class OrgnineCaseProjectFaultLog(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    device_type = models.CharField(max_length=4, blank=True, null=True)
    device_id = models.CharField(max_length=128, blank=True, null=True)
    device_name = models.CharField(max_length=128, blank=True, null=True)
    fault_start_time = models.DateTimeField(blank=True, null=True)
    fault_end_time = models.DateTimeField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_project_fault_log'


class OrgnineCaseProjectFaultLogCopy(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    device_type = models.CharField(max_length=4, blank=True, null=True)
    device_id = models.CharField(max_length=128, blank=True, null=True)
    device_name = models.CharField(max_length=128, blank=True, null=True)
    fault_start_time = models.DateTimeField(blank=True, null=True)
    fault_end_time = models.DateTimeField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_project_fault_log_copy'


class OrgnineCaseProjectMonitorConfig(models.Model):
    service_id = models.CharField(max_length=64, blank=True, null=True)
    service_host = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=128, blank=True, null=True)
    device_name = models.CharField(max_length=128, blank=True, null=True)
    device_ip = models.CharField(max_length=128, blank=True, null=True)
    device_port = models.CharField(max_length=128, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_project_monitor_config'
        unique_together = (('service_host', 'device_id'),)


class OrgnineCaseProjectStatus(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    project_status = models.CharField(max_length=4, blank=True, null=True)
    service_status = models.CharField(max_length=4, blank=True, null=True)
    camera_status = models.CharField(max_length=4, blank=True, null=True)
    integrated_machine_status = models.CharField(max_length=4, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_project_status'


class OrgnineCaseSenseSecret(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    sense_ak = models.CharField(max_length=128, blank=True, null=True)
    sense_sk = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=4, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_case_sense_secret'


class OrgnineConfigEmailSetting(models.Model):
    smtp_host = models.CharField(max_length=128, blank=True, null=True)
    smtp_port = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    pwd = models.CharField(max_length=64, blank=True, null=True)
    send_nick_name = models.CharField(max_length=64, blank=True, null=True)
    show_nick_name = models.CharField(max_length=64, blank=True, null=True)
    email_type = models.CharField(max_length=64, blank=True, null=True)
    pop_imap_server = models.CharField(max_length=64, blank=True, null=True)
    pop_imap_port = models.CharField(max_length=64, blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_email_setting'


class OrgnineConfigIpPool(models.Model):
    ip = models.CharField(max_length=64, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    ip_status = models.CharField(max_length=3, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_ip_pool'


class OrgnineConfigLogistics(models.Model):
    lname = models.CharField(max_length=128, blank=True, null=True)
    lzone = models.CharField(max_length=128, blank=True, null=True)
    lprov = models.CharField(max_length=128, blank=True, null=True)
    lcity = models.CharField(max_length=128, blank=True, null=True)
    larea = models.CharField(max_length=128, blank=True, null=True)
    laddr = models.CharField(max_length=128, blank=True, null=True)
    lalladdress = models.CharField(max_length=555, blank=True, null=True)
    lusername = models.CharField(max_length=128, blank=True, null=True)
    lphone = models.CharField(max_length=64, blank=True, null=True)
    lcode = models.CharField(max_length=64, blank=True, null=True)
    lstate = models.IntegerField(blank=True, null=True)
    limage = models.CharField(max_length=555, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_logistics'


class OrgnineConfigMessageTemplate(models.Model):
    code = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    template_title = models.CharField(max_length=128, blank=True, null=True)
    template_desc = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_message_template'


class OrgnineConfigMobileSetting(models.Model):
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    describes = models.CharField(max_length=64, blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_mobile_setting'


class OrgnineConfigMobileSettingInfo(models.Model):
    mobile_setting_id = models.IntegerField(blank=True, null=True)
    label_text = models.CharField(max_length=64, blank=True, null=True)
    input_type = models.CharField(max_length=64, blank=True, null=True)
    config_key = models.CharField(max_length=64, blank=True, null=True)
    config_value = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    describes = models.CharField(max_length=64, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_mobile_setting_info'


class OrgnineConfigPayType(models.Model):
    pay_type_name = models.CharField(max_length=128, blank=True, null=True)
    pay_type_desc = models.CharField(max_length=128, blank=True, null=True)
    pay_type_state = models.IntegerField(blank=True, null=True)
    pay_type_logo = models.CharField(max_length=128, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_pay_type'


class OrgnineConfigPayWay(models.Model):
    pay_code = models.CharField(max_length=128, blank=True, null=True)
    pay_name = models.CharField(max_length=128, blank=True, null=True)
    pay_desc = models.CharField(max_length=128, blank=True, null=True)
    pay_state = models.IntegerField(blank=True, null=True)
    pay_logo = models.CharField(max_length=128, blank=True, null=True)
    pay_type_id = models.IntegerField(blank=True, null=True)
    pay_config1 = models.CharField(max_length=512, blank=True, null=True)
    pay_config2 = models.CharField(max_length=512, blank=True, null=True)
    pay_config3 = models.CharField(max_length=512, blank=True, null=True)
    pay_config4 = models.CharField(max_length=512, blank=True, null=True)
    pay_config5 = models.CharField(max_length=512, blank=True, null=True)
    pay_config6 = models.CharField(max_length=512, blank=True, null=True)
    pay_config7 = models.CharField(max_length=512, blank=True, null=True)
    pay_config8 = models.CharField(max_length=512, blank=True, null=True)
    pay_config9 = models.CharField(max_length=512, blank=True, null=True)
    pay_config10 = models.CharField(max_length=512, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_pay_way'


class OrgnineConfigPlatform(models.Model):
    platform_name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    platform_logo = models.CharField(max_length=256, blank=True, null=True)
    platform_name_zh = models.CharField(max_length=64, blank=True, null=True)
    country_count = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_platform'


class OrgnineConfigPlatformCountry(models.Model):
    country_name = models.CharField(max_length=64, blank=True, null=True)
    short_name = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=64, blank=True, null=True)
    time_zone = models.CharField(max_length=64, blank=True, null=True)
    gmt_time_zone = models.CharField(max_length=64, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_platform_country'
        unique_together = (('country_name', 'short_name'),)


class OrgnineConfigPlatformCountryRef(models.Model):
    platform_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=256, blank=True, null=True)
    marketplace_id = models.CharField(max_length=64, blank=True, null=True)
    interface_addr = models.CharField(max_length=100, blank=True, null=True)
    belong_to_area = models.CharField(max_length=64, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_platform_country_ref'
        unique_together = (('platform_id', 'country_id'),)


class OrgnineConfigSyncDate(models.Model):
    mid = models.IntegerField(blank=True, null=True)
    sync_type = models.CharField(max_length=64, blank=True, null=True)
    sync_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_config_sync_date'


class OrgnineMember(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    pwd = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    send_mobile_code = models.CharField(max_length=256, blank=True, null=True)
    last_login_ip = models.CharField(max_length=256, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    referid = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=256, blank=True, null=True)
    no = models.CharField(max_length=256, blank=True, null=True)
    member_level = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=256, blank=True, null=True)
    nick_name = models.CharField(max_length=256, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    valid_email = models.CharField(max_length=256, blank=True, null=True)
    valid_mobile = models.CharField(max_length=256, blank=True, null=True)
    zone = models.CharField(max_length=256, blank=True, null=True)
    province = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=555, blank=True, null=True)
    postcode = models.CharField(max_length=256, blank=True, null=True)
    qq = models.CharField(max_length=256, blank=True, null=True)
    msn = models.CharField(max_length=256, blank=True, null=True)
    blog = models.CharField(max_length=256, blank=True, null=True)
    wechat = models.CharField(max_length=256, blank=True, null=True)
    comsume_amount = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    gold = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    capital = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    ccapital = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    credit = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    credit_max = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    credit_over = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    source_mode = models.CharField(max_length=555, blank=True, null=True)
    pay_pwd = models.CharField(max_length=555, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_member'


class OrgnineMemberAccount(models.Model):
    ma_type = models.IntegerField(blank=True, null=True)
    ma_account = models.CharField(max_length=555, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_member_account'


class OrgnineMemberLevel(models.Model):
    level_logo = models.CharField(max_length=128, blank=True, null=True)
    level_name = models.CharField(max_length=128, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    level_start = models.IntegerField(blank=True, null=True)
    level_end = models.IntegerField(blank=True, null=True)
    discount = models.DecimalField(max_digits=32, decimal_places=4, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_member_level'


class OrgnineMemberMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    parent_ids = models.CharField(max_length=500)
    sort = models.IntegerField(blank=True, null=True)
    href = models.CharField(max_length=256, blank=True, null=True)
    menu_type = models.CharField(max_length=1, blank=True, null=True)
    visible = models.CharField(max_length=1, blank=True, null=True)
    permission = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    is_show = models.CharField(max_length=64, blank=True, null=True)
    menu_level = models.IntegerField(blank=True, null=True)
    menu_code = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    purpose = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_member_menu'


class OrgnineMemberRole(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    ename = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_member_role'


class OrgnineMemberRoleMenu(models.Model):
    role_id = models.IntegerField(primary_key=True)
    menu_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orgnine_member_role_menu'
        unique_together = (('role_id', 'menu_id'),)


class OrgnineMemberUserNode(models.Model):
    user_id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orgnine_member_user_node'
        unique_together = (('user_id', 'node_id'),)


class OrgnineMemberUserProject(models.Model):
    user_id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orgnine_member_user_project'
        unique_together = (('user_id', 'project_id'),)


class OrgnineMemberUserRole(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orgnine_member_user_role'
        unique_together = (('user_id', 'role_id'),)


class OrgnineServiceBusiness(models.Model):
    service_name = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(max_length=64, blank=True, null=True)
    we_chat = models.CharField(max_length=64, blank=True, null=True)
    service_domain = models.CharField(max_length=64, blank=True, null=True)
    project_name = models.CharField(max_length=64, blank=True, null=True)
    service_ip = models.CharField(max_length=64, blank=True, null=True)
    service_port = models.CharField(max_length=64, blank=True, null=True)
    service_valid_start_date = models.DateTimeField(blank=True, null=True)
    service_valid_end_date = models.DateTimeField(blank=True, null=True)
    machine_code = models.TextField(blank=True, null=True)
    license_code = models.TextField(blank=True, null=True)
    service_status = models.CharField(max_length=1, blank=True, null=True)
    send_status = models.CharField(max_length=2, blank=True, null=True)
    remarks = models.CharField(max_length=1024, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_service_business'


class OrgnineServiceVersion(models.Model):
    version_no = models.CharField(max_length=64, blank=True, null=True)
    version_name = models.CharField(max_length=64, blank=True, null=True)
    version_content = models.CharField(max_length=1024, blank=True, null=True)
    version_type = models.CharField(max_length=1, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_service_version'


class OrgnineWebsiteAd(models.Model):
    ad_full_title = models.CharField(max_length=555, blank=True, null=True)
    ad_short_title = models.CharField(max_length=555, blank=True, null=True)
    ad_type = models.IntegerField(blank=True, null=True)
    ad_img_url = models.CharField(max_length=555, blank=True, null=True)
    ad_content = models.CharField(max_length=555, blank=True, null=True)
    ad_sn = models.IntegerField(blank=True, null=True)
    ad_c_count = models.IntegerField(blank=True, null=True)
    ad_f_count = models.IntegerField(blank=True, null=True)
    ad_desc = models.CharField(max_length=555, blank=True, null=True)
    ad_link_type = models.IntegerField(blank=True, null=True)
    ad_link = models.CharField(max_length=555, blank=True, null=True)
    ad_state = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_ad'


class OrgnineWebsiteArticle(models.Model):
    article_name = models.CharField(max_length=555, blank=True, null=True)
    article_desc = models.TextField(blank=True, null=True)
    article_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    article_sort = models.IntegerField(blank=True, null=True)
    seo_title = models.CharField(max_length=555, blank=True, null=True)
    seo_keywords = models.CharField(max_length=555, blank=True, null=True)
    seo_description = models.CharField(max_length=555, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_article'


class OrgnineWebsiteChannel(models.Model):
    channel_name = models.CharField(max_length=555, blank=True, null=True)
    channel_alias_name = models.CharField(max_length=555, blank=True, null=True)
    channel_desc = models.CharField(max_length=255, blank=True, null=True)
    channel_exclusive = models.IntegerField(blank=True, null=True)
    channel_state = models.IntegerField(blank=True, null=True)
    seo_title = models.CharField(max_length=555, blank=True, null=True)
    seo_keywords = models.CharField(max_length=555, blank=True, null=True)
    seo_description = models.CharField(max_length=555, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_channel'


class OrgnineWebsiteChannelExhibitionRel(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    exhibition_id = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_channel_exhibition_rel'


class OrgnineWebsiteConfigure(models.Model):
    website_type = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    label_type = models.CharField(max_length=64, blank=True, null=True)
    dict_type = models.CharField(max_length=64, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_configure'


class OrgnineWebsiteExhibition(models.Model):
    exhibition_name = models.CharField(max_length=200, blank=True, null=True)
    exhibition_alias_name = models.CharField(max_length=200, blank=True, null=True)
    exhibition_desc = models.CharField(max_length=555, blank=True, null=True)
    exhibition_type = models.IntegerField(blank=True, null=True)
    exhibition_state = models.IntegerField(blank=True, null=True)
    exhibition_sort = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    exhibition_limit = models.IntegerField(blank=True, null=True)
    exhibition_exclusive = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=555, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_exhibition'


class OrgnineWebsiteExhibitionDataRel(models.Model):
    exhibition_id = models.IntegerField(blank=True, null=True)
    data_id = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=555, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_exhibition_data_rel'


class OrgnineWebsiteFlink(models.Model):
    flink_title = models.CharField(max_length=555, blank=True, null=True)
    flink_img = models.CharField(max_length=555, blank=True, null=True)
    flink_count = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    flink_url = models.CharField(max_length=555, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgnine_website_flink'


class QrtzBlobTriggers(models.Model):
    sched_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='sched_name', primary_key=True)
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    blob_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_blob_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzCalendars(models.Model):
    sched_name = models.CharField(primary_key=True, max_length=120)
    calendar_name = models.CharField(max_length=200)
    calendar = models.TextField()

    class Meta:
        managed = False
        db_table = 'qrtz_calendars'
        unique_together = (('sched_name', 'calendar_name'),)


class QrtzCronTriggers(models.Model):
    sched_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='sched_name', primary_key=True)
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    cron_expression = models.CharField(max_length=200)
    time_zone_id = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_cron_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzFiredTriggers(models.Model):
    sched_name = models.CharField(primary_key=True, max_length=120)
    entry_id = models.CharField(max_length=95)
    trigger_name = models.CharField(max_length=200)
    trigger_group = models.CharField(max_length=200)
    instance_name = models.CharField(max_length=200)
    fired_time = models.BigIntegerField()
    sched_time = models.BigIntegerField()
    priority = models.IntegerField()
    state = models.CharField(max_length=16)
    job_name = models.CharField(max_length=200, blank=True, null=True)
    job_group = models.CharField(max_length=200, blank=True, null=True)
    is_nonconcurrent = models.CharField(max_length=1, blank=True, null=True)
    requests_recovery = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_fired_triggers'
        unique_together = (('sched_name', 'entry_id'),)


class QrtzJobDetails(models.Model):
    sched_name = models.CharField(primary_key=True, max_length=120)
    job_name = models.CharField(max_length=200)
    job_group = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True, null=True)
    job_class_name = models.CharField(max_length=250)
    is_durable = models.CharField(max_length=1)
    is_nonconcurrent = models.CharField(max_length=1)
    is_update_data = models.CharField(max_length=1)
    requests_recovery = models.CharField(max_length=1)
    job_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_job_details'
        unique_together = (('sched_name', 'job_name', 'job_group'),)


class QrtzLocks(models.Model):
    sched_name = models.CharField(primary_key=True, max_length=120)
    lock_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'qrtz_locks'
        unique_together = (('sched_name', 'lock_name'),)


class QrtzPausedTriggerGrps(models.Model):
    sched_name = models.CharField(primary_key=True, max_length=120)
    trigger_group = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'qrtz_paused_trigger_grps'
        unique_together = (('sched_name', 'trigger_group'),)


class QrtzSchedulerState(models.Model):
    sched_name = models.CharField(primary_key=True, max_length=120)
    instance_name = models.CharField(max_length=200)
    last_checkin_time = models.BigIntegerField()
    checkin_interval = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'qrtz_scheduler_state'
        unique_together = (('sched_name', 'instance_name'),)


class QrtzSimpleTriggers(models.Model):
    sched_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='sched_name', primary_key=True)
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    repeat_count = models.BigIntegerField()
    repeat_interval = models.BigIntegerField()
    times_triggered = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'qrtz_simple_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzSimpropTriggers(models.Model):
    sched_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='sched_name', primary_key=True)
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    str_prop_1 = models.CharField(max_length=512, blank=True, null=True)
    str_prop_2 = models.CharField(max_length=512, blank=True, null=True)
    str_prop_3 = models.CharField(max_length=512, blank=True, null=True)
    int_prop_1 = models.IntegerField(blank=True, null=True)
    int_prop_2 = models.IntegerField(blank=True, null=True)
    long_prop_1 = models.BigIntegerField(blank=True, null=True)
    long_prop_2 = models.BigIntegerField(blank=True, null=True)
    dec_prop_1 = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    dec_prop_2 = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    bool_prop_1 = models.CharField(max_length=1, blank=True, null=True)
    bool_prop_2 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_simprop_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class QrtzTriggers(models.Model):
    sched_name = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='sched_name', primary_key=True)
    trigger_name = models.CharField(max_length=200)
    trigger_group = models.CharField(max_length=200)
    job_name = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='job_name')
    job_group = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='job_group')
    description = models.CharField(max_length=250, blank=True, null=True)
    next_fire_time = models.BigIntegerField(blank=True, null=True)
    prev_fire_time = models.BigIntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    trigger_state = models.CharField(max_length=16)
    trigger_type = models.CharField(max_length=8)
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField(blank=True, null=True)
    calendar_name = models.CharField(max_length=200, blank=True, null=True)
    misfire_instr = models.SmallIntegerField(blank=True, null=True)
    job_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class SysConfig(models.Model):
    config_id = models.AutoField(primary_key=True)
    config_name = models.CharField(max_length=100, blank=True, null=True)
    config_key = models.CharField(max_length=100, blank=True, null=True)
    config_value = models.CharField(max_length=1000, blank=True, null=True)
    config_type = models.CharField(max_length=1, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_config'


class SysDept(models.Model):
    dept_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ancestors = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.CharField(max_length=30, blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    leader = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    del_flag = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dept'


class SysDictData(models.Model):
    dict_code = models.AutoField(primary_key=True)
    dict_sort = models.IntegerField(blank=True, null=True)
    dict_label = models.CharField(max_length=100, blank=True, null=True)
    dict_value = models.CharField(max_length=100, blank=True, null=True)
    dict_type = models.CharField(max_length=100, blank=True, null=True)
    css_class = models.CharField(max_length=100, blank=True, null=True)
    list_class = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dict_data'


class SysDictType(models.Model):
    dict_id = models.AutoField(primary_key=True)
    dict_name = models.CharField(max_length=100, blank=True, null=True)
    dict_type = models.CharField(unique=True, max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dict_type'


class SysJob(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=64)
    job_group = models.CharField(max_length=64)
    method_name = models.CharField(max_length=500, blank=True, null=True)
    method_params = models.CharField(max_length=200, blank=True, null=True)
    cron_expression = models.CharField(max_length=255, blank=True, null=True)
    misfire_policy = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_job'
        unique_together = (('job_id', 'job_name', 'job_group'),)


class SysJobLog(models.Model):
    job_log_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=64)
    job_group = models.CharField(max_length=64)
    method_name = models.CharField(max_length=500, blank=True, null=True)
    method_params = models.CharField(max_length=200, blank=True, null=True)
    job_message = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    exception_info = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_job_log'


class SysLogininfor(models.Model):
    info_id = models.AutoField(primary_key=True)
    login_name = models.CharField(max_length=50, blank=True, null=True)
    ipaddr = models.CharField(max_length=50, blank=True, null=True)
    login_location = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_logininfor'


class SysMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=50)
    parent_id = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    menu_type = models.CharField(max_length=1, blank=True, null=True)
    visible = models.CharField(max_length=1, blank=True, null=True)
    perms = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysNotice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=50)
    notice_type = models.CharField(max_length=2)
    notice_content = models.CharField(max_length=500)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_notice'


class SysOperLog(models.Model):
    oper_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    business_type = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)
    operator_type = models.IntegerField(blank=True, null=True)
    oper_name = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.CharField(max_length=50, blank=True, null=True)
    oper_url = models.CharField(max_length=255, blank=True, null=True)
    oper_ip = models.CharField(max_length=30, blank=True, null=True)
    oper_location = models.CharField(max_length=255, blank=True, null=True)
    oper_param = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    error_msg = models.CharField(max_length=2000, blank=True, null=True)
    oper_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_oper_log'


class SysPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_code = models.CharField(max_length=64)
    post_name = models.CharField(max_length=50)
    post_sort = models.IntegerField()
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_post'


class SysRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=30)
    role_key = models.CharField(max_length=100)
    role_sort = models.IntegerField()
    data_scope = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1)
    del_flag = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleDept(models.Model):
    role_id = models.IntegerField(primary_key=True)
    dept_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role_dept'
        unique_together = (('role_id', 'dept_id'),)


class SysRoleMenu(models.Model):
    role_id = models.IntegerField(primary_key=True)
    menu_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role_menu'
        unique_together = (('role_id', 'menu_id'),)


class SysUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    dept_id = models.IntegerField(blank=True, null=True)
    login_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=2, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=11, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    salt = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    del_flag = models.CharField(max_length=1, blank=True, null=True)
    login_ip = models.CharField(max_length=20, blank=True, null=True)
    login_date = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserOnline(models.Model):
    sessionid = models.CharField(db_column='sessionId', primary_key=True, max_length=50)  # Field name made lowercase.
    login_name = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.CharField(max_length=50, blank=True, null=True)
    ipaddr = models.CharField(max_length=50, blank=True, null=True)
    login_location = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    start_timestamp = models.DateTimeField(blank=True, null=True)
    last_access_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_online'


class SysUserPost(models.Model):
    user_id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_user_post'
        unique_together = (('user_id', 'post_id'),)


class SysUserRole(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_user_role'
        unique_together = (('user_id', 'role_id'),)