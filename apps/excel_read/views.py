import threading
import time

import xlrd
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from channelaudit.models import CaseProject
from common.models import CaseChannel
from excel_read.serializers import ReadModelSerializer
from help.audit_monitor import get_result
from help.util import time_to_timestamp, time_to_date
from audit.settings import pool
from datetime import datetime

from tatistics.models import 统计


class ReadModelViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ReadModelSerializer

    def create(self, request, *args, **kwargs):
        global r
        project_id = request.data["project"]
        wb = xlrd.open_workbook(
            filename=None, file_contents=request.FILES["xl"].read())  # 关键点在于这里
        table = wb.sheet_by_name("渠道稽核")
        row = table.nrows
        结果 = {}
        r = {}
        t = time.time()
        tx=time.time()
        number=0
        for i in range(1, row):
            value = {
                "custom_name": table.cell(i, 0).value,
                "customer_id_card": table.cell(i, 1).value,
                "customer_phone": table.cell(i, 2).value,
                "customer_status": table.cell(i, 3).value,
                "first_look_time":  datetime( *xlrd.xldate_as_tuple(table.cell(i, 4).value,0)),
                "report_time": datetime( *xlrd.xldate_as_tuple(table.cell(i, 5).value,0)),
                "sign_time": datetime( *xlrd.xldate_as_tuple(table.cell(i, 6).value,0)),
                "dynatown": table.cell(i, 7).value,
                "agent": table.cell(i, 8).value,
                "channel_company": table.cell(i, 9).value,
                "sign_room_num": table.cell(i, 10).value,
            }
            # write_table(value,project_id,结果,i)
            number+=1
            t=time.time()
            pool.apply_async(write_table, args=(value, project_id, 结果, i))
            # r[i] = (threading.Thread(target=write_table, args=(value, project_id, 结果, i)))
            # r[i].start()

        # for i in range(1, row):
        #         r[i].join()
        pool.close()
        pool.join()
        return Response({"time": time.time() - tx, "result": 结果})


def write_table(value: dict, project_id, 结果, i):
    try:
        projcet = CaseProject.objects.get(id=project_id)
        instance,new = CaseChannel.objects.get_or_create(customer_id_card=value["customer_id_card"], project=projcet, )
        instance.custom_name = value["custom_name"]
        instance.customer_phone = value["customer_phone"]
        instance.customer_status = value["customer_status"]
        instance.first_look_time = str(value["first_look_time"])
        instance.report_time = time_to_timestamp(value["report_time"])
        instance.sign_time = str(value["sign_time"])
        instance.dynatown = value["dynatown"]
        instance.agent = value["agent"]
        instance.channel_company = value["channel_company"]
        instance.sign_room_num = value["sign_room_num"]
        结果[i] = True
        # lock.acquire()
        instance.save()
        get_result(instance)
        # lock.release()
    except Exception as e:
        结果[i] = str(e)