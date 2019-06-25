import requests
from .get_sensego_class import NonceBase64, Trace
import json


def sensego_multiidentify(ak: str, sk: str, group_id: str, face_image: str, id_image=None):
    p1 = NonceBase64(ak, sk, group_id, face_image, id_image)
    r = requests.post('https://icloud.sensetime.com/sensego/v2.0/mingyuan/multiidentify', data=p1.get_dic())
    return r.json()


def sensego_trace(ak: str, sk: str, group_id: str, person_id: str, limit=None):
    p = Trace(ak, sk, group_id, person_id, limit)
    r = requests.post('https://icloud.sensetime.com/sensego/v2.0/mingyuan/trace', data=p.get_dic())
    return r.json()
