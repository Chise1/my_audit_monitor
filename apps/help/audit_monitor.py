"""
渠道稽核方法
"""
from common.models import CaseIdentify, CaseIdentifyConfidence
from common.models import CaseChannel
from help.util import timestamp_to_time, time_to_timestamp
from help.访问sensego2 import sensego_multiidentify
import base64


def case(instance: CaseIdentify):
    """
    刷证的时候调用
    :type instance: CaseIdentify
    :param instance:
    :return:
    """
    id_number = instance.id_number
    project = instance.project
    ak = project.sensetimeId.ak
    sk = project.sensetimeId.sk
    group_id = project.group_id
    # 读取imagefiled的文件
    face_image = instance.face_image.open(mode='rb').read()
    id_image = instance.id_image.open(mode='rb').read()

    face_image = base64.b64encode(face_image).decode()
    id_image = base64.b64encode(id_image).decode()
    result = sensego_multiidentify(ak, sk, group_id, face_image, id_image)
    if str(result["error_code"]) != "0":
        return False
    persons = result["results"]
    try:
        # 有报备记录
        channel = CaseChannel.objects.get(customer_id_card=id_number, project=project)
        baobei_time = channel.report_time
        p = 更新到访记录(persons, project, id_number)
        if channel.report_time == "/":
            for ps in p:
                ps.customer_type = 5
                ps.save()
            return True
        else:
            for ps in p:
                if int(baobei_time) - int(ps.first_snap_time) < project.node.fly_sheet_audit_tolerance * 60:
                    # 报备-首次抓拍<稽核时间
                    if project.node.avert_carrying_capacity_status == "on":
                        # 截客打开
                        if int(ps.first_snap_time) - int(
                                baobei_time) < project.node.avert_carrying_capacity_tolerance:
                            # 首次抓拍-报备<截客容差
                            ps.customer_type = 2
                        else:
                            ps.customer_type = 5
                    else:
                        ps.customer_type = 5
                else:
                    # 报备时间-首次抓拍>稽核时间
                    ps.customer_type = 1

                if int(ps.first_snap_time) == 2500000000 and (
                        ps.customer_type == 5 or ps.customer_type == 1 or ps.customer_type == 2):
                    ps.customer_type = 8
                ps.save()

    except Exception as e:
        print(e)
        # 仅刷证
        try:
            p = 更新到访记录(persons, project, id_number)
            for ps in p:
                ps.save()
            return True
        except Exception as e:
            print(e)
            return False


def get_result(instance):
    """
    录入结果值,instance提前保存
    :param instance:
    :return:
    """
    try:
        if isinstance(instance, CaseIdentify):
            # 刷证
            case(instance)
        elif isinstance(instance, CaseChannel):
            # 报备
            id_number = instance.customer_id_card
            project = instance.project
            try:
                # 有刷证记录
                instance2 = CaseIdentify.objects.get(id_number=id_number, project=project)
                case(instance2)
            except:
                # 没有刷证记录
                t = str(2500000000)
                p_high = CaseIdentifyConfidence.objects.get_or_create(project=project, id_number=id_number, confidence="high",
                                                                customer_type=3)[0]
                p_high.first_snap_time=t
                p_medium = CaseIdentifyConfidence.objects.get_or_create(project=project, id_number=id_number,
                                                                 confidence="medium",
                                                                 customer_type=3)[0]
                p_medium.first_snap_time=t
                p_low = CaseIdentifyConfidence.objects.get_or_create(project=project, id_number=id_number,
                                                              confidence="low",  customer_type=3)[0]
                p_low.first_snap_time=t
                p_high.save()
                p_medium.save()
                p_low.save()
    except Exception as e:
        print(e)


def 更新到访记录(persons, project, id_number):
    # 仅刷证
    t = str(2500000000)
    try:
        p_high = CaseIdentifyConfidence.objects.get(project=project, id_number=id_number, confidence="high",
                                                    )
    except:
        p_high = CaseIdentifyConfidence.objects.create(project=project, id_number=id_number, confidence="high",
                                                       first_snap_time=t)
    try:
        p_medium = CaseIdentifyConfidence.objects.get(project=project, id_number=id_number, confidence="medium",
                                                      )
    except:
        p_medium = CaseIdentifyConfidence.objects.create(project=project, id_number=id_number, confidence="medium",
                                                         first_snap_time=t)
    try:
        p_low = CaseIdentifyConfidence.objects.get(project=project, id_number=id_number, confidence="low",
                                                   )
    except:
        p_low = CaseIdentifyConfidence.objects.create(project=project, id_number=id_number, confidence="low",
                                                      first_snap_time=t)

    for person in persons:
        arrived_at = person["arrived_at"].split(" ")
        arrived_at = arrived_at[0] + " " + arrived_at[1]
        ft = time_to_timestamp(arrived_at)
        if ft > 3000000000:
            ft = ft // 1000
        if person["confidence"] == "high":
            if int(p_high.first_snap_time) > ft:
                p_high.first_snap_time = str(ft)
            if int(p_medium.first_snap_time) > ft:
                p_medium.first_snap_time = str(ft)
            if int(p_low.first_snap_time) > ft:
                p_low.first_snap_time = str(ft)
        elif person["confidence"] == "medium":
            if int(p_medium.first_snap_time) > ft:
                p_medium.first_snap_time = str(ft)
            if int(p_low.first_snap_time) > ft:
                p_low.first_snap_time = str(ft)
        else:
            if int(p_low.first_snap_time) > ft:
                p_low.first_snap_time = str(ft)
    return (p_high, p_medium, p_low)
