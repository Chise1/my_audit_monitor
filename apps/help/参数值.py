import time

from audit.settings import service_version


def auth_true(token: str) -> dict:
    return {
        "code": 0,
        "message": "success",
        "data": {
            "token": token,
            "timestamp": str(int(time.time() * 1000)),
            "version": service_version
        }
    }


def auth_false(msg: str = "illegal request") -> dict:
    return {
        "code": 401,
        "message": msg,
    }


def heartbeat_true() -> dict:
    return {
        "code": 0,
        "message": "success",
        "data": {
            "version": service_version,
            "timestamp": int(time.time() * 1000),
        }
    }


def heartbeat_false(msg: str) -> dict:
    return {
        "code": 401,
        "message": msg,  # 服务器自定义
    }


def upload_data_true() -> dict:
    return {
        "code": 0,
        "message": "upload successful"
    }


def upload_data_false(error: str = "token is invalid"):
    return {
        "code": 401,
        "message": error,
    }


# 测试返回数据异常结果
upload_data_false_test = {
    # "code": 401,
    "code": 401,
    "message": "你是个傻逼"
}
create_project_true = {
    "code": 0,
    "message": "create successful"
}
create_project_false_401 = {
    "code": 401,
    "message": "project name is null!"
}
create_project_false_402 = {
    "code": 402,
    "message": "invalid !"
}
create_project_false_403 = {
    "code": 403,
    "message": "该项目已存在！"
}
