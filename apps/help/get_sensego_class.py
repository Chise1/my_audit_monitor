import base64
import hashlib
import hmac
import time
import uuid


class Nonce():
    def __init__(self, ak, sk, group_id, face_image):
        self.face_image = base64.b64encode(face_image).decode()
        self.id_image = None
        self.ak = ak
        self.sk = sk
        self.group_id = group_id
        self.sign = self.get_sign()

    def get_sign(self):
        self.ts = str(int(time.time()))

        # self.nonce = str(uuid.uuid1()).replace("-", "")
        self.nonce = str(uuid.uuid1()).replace("-", "")
        a = [self.ak, self.nonce, self.ts]
        # a = [self.ak, 'ZPMxNpPhmrPzQj27AGKijM3FmEcHW4BY', '1550032562']
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        if a[0] > a[2]:
            a[0], a[2] = a[2], a[0]
        if a[1] > a[2]:
            a[1], a[2] = a[2], a[1]
        join_str = "".join(a)
        return hmac.new(self.sk.encode(), join_str.encode(), hashlib.sha256).hexdigest()

    def get_dic(self):
        dic = {
            'ak': self.ak,
            'nonce': self.nonce,
            'sign': self.sign,
            'ts': self.ts,
            'group_id': self.group_id,
            'face_image': self.face_image
        }
        if self.id_image != None:
            dic["id_image"] = self.id_image
        return dic


class NonceBase64(Nonce):
    '''base64图片'''

    def __init__(self, ak, sk, group_id, face_image, id_image=None):
        self.face_image = face_image
        self.id_image = None
        if id_image is not None:
            self.id_image = id_image

        self.ak = ak
        self.sk = sk
        self.group_id = group_id
        self.sign = self.get_sign()


class Trace(Nonce):
    def __init__(self, ak, sk, group_id, person_id, limit=None):
        self.limit = None
        if limit is not None:
            self.limit = limit

        self.person_id = person_id
        self.ak = ak
        self.sk = sk
        self.group_id = group_id
        self.sign = self.get_sign()

    def get_dic(self):
        dic = {
            'ak': self.ak,
            'nonce': self.nonce,
            'sign': self.sign,
            'ts': self.ts,
            'group_id': self.group_id,
            'person_id': self.person_id
        }
        if self.limit is not None:
            dic["limit"] = self.limit
        return dic
