import requests
import base64

from help.get_sensego_class import NonceBase64
def multiidentify(base64picture):
    p1 = NonceBase64(base64picture)
    r = requests.post('https://icloud.sensetime.com/sensego/v2.0/mingyuan/multiidentify', data=p1.get_dic())
    res = r.json()
    print(res)


# with open("ID020P18H00294_1556163151614.jpg", "rb") as f:
#     x = f.read()
#     print(x)
#     pic = base64.b64encode(x)
#     multiidentify(pic)


with open(r"C:\Users\Cs\Desktop\0.jpg", "rb") as f:
    face_image = base64.b64encode(f.read())
    with open(r"C:\Users\Cs\Desktop\1.jpg", "rb") as f2:
        id_image = base64.b64encode(f2.read())
        p1 = NonceBase64(face_image, id_image)
        r = requests.post('https://icloud.sensetime.com/sensego/v2.0/mingyuan/multiidentify', data=p1.get_dic())
        print(p1.get_dic())
        res = r.json()
        print(res)