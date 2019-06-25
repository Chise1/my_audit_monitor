import xadmin
from .models import CaseChannel, CaseIdentify, CaseIdentifyConfidence


class CaseChannelAdmin(object):
    list_display = ("custom_name", "customer_id_card", "report_time",)
    # list_display=("custom_name","customer_id_card","report_time","my_identify__verify_time","my_confidence")
    # list_fields=("project","my_confidence__confidence","my_identify__verify_time","is_del")
    search_fields = ("customer_id_card", "customer_phone","custom_name")


class CaseIdentityAdmin(object):
    list_display = ("project", "name", "id_number", "verify_time")
    search_fields = ("id_number","name")

class CaseIdentityConfidenceAdmin(object):
    list_display = ("project", "id_number","first_snap_time", "customer_type", "confidence")
    search_fields = ("id_number", )
    list_filter=("confidence","customer_type")


xadmin.site.register(CaseChannel, CaseChannelAdmin)
xadmin.site.register(CaseIdentify, CaseIdentityAdmin)
xadmin.site.register(CaseIdentifyConfidence, CaseIdentityConfidenceAdmin)
