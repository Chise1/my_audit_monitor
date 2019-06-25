import hashlib
import hmac
import time
import uuid
from hashlib import md5

# 创建token
from audit.settings import salt
from channelaudit.models import CaseProjectDevice
from senseid.models import SenseID


def test_token(data):
    senseid = SenseID.objects.get(device_id=data["device_id"])
    if senseid.token == data["token"]:
        return True
    else:
        return False


def set_token(device_id: str, timestamp):
    """
    生成token并保存到对应senseid并返回token
    :param device_id:一体机id
    :return:
    """
    try:
        senseid = SenseID.objects.get(device_id=device_id)
    except:
        try:
            pro=CaseProjectDevice.objects.get(device_id=device_id)
            senseid = SenseID(device_id=device_id, project_device=pro)
        except :
            return None
    if int(timestamp) - int(senseid.token_time) < 60 * 1000:
        return senseid.token
    else:
        project = senseid.project_device.project
        ak = project.sensetimeId.ak
        sk = project.sensetimeId.sk
        ts = str(int(time.time() * 1000))
        nonce = str(uuid.uuid1()).replace("-", "")
        a = [ak, nonce, ts]
        join_str = "".join(a)
        token = hmac.new(sk.encode(), join_str.encode(), hashlib.sha256).hexdigest()
        senseid.token = token
        senseid.token_time = ts
        senseid.save()
        return token

def check_token(device_id: str,token:str)->bool:
    try:
        senseid = SenseID.objects.get(device_id=device_id)
        if senseid.token==token:
            return True
        else:
            return False
    except :
        return False

def get_token2(data: dict) -> str:
    """
    获取数据库存储的token
    :param data:
    :return:
    """
    sense_id = SenseID.objects.get(device_id=data["device_id"])
    return sense_id.token


# 获取签名
def get_sign(device_id: str, timestamp, version: str) -> str:  # salt 盐
    """
    取一个字符串的hash值
    :param device_id: 一体机id
    :param timestamp: 一体机时间戳
    :param version: 一体机版本
    :return: Bool
    """
    # 提高字符串的复杂度
    params: str = "device_id=" + str(device_id) + "&timestamp=" + str(timestamp) + "&version=" + str(version)
    # 加盐
    params += salt
    # 取str　hash值
    sh = md5()
    sh.update(params.encode("utf-8"))
    sign = sh.hexdigest()
    return str(sign)


def check_sign(device_id: str, timestamp: str, version: str, sign: str) -> bool:
    """
    sign验证
    :param device_id: 一体机id
    :param timestamp: 时间戳
    :param version: 版本号
    :param sign: 一体机sign值
    :return: Bool
    """

    if sign == get_sign(device_id, timestamp, version):
        return True
    else:
        return False
