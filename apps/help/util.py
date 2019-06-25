# 时间戳处理
import datetime
import time


def timestamp_to_10(timestamp):
    t = int(timestamp)
    while t > 3000000000:
        t = t // 10
    while t < 1000000000:
        t = int(timestamp * 10)
    return t


def timestamp_to_time(timeStamp):
    timeStamp = int(timeStamp)
    if timeStamp > 3000000000:
        timeArray = time.localtime(int(timeStamp) // 1000)
        x = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    else:
        timeArray = time.localtime(int(timeStamp))
        x = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return x


def time_to_timestamp(time___):
    # # 转换成时间数组
    # timeArray = time.strptime(time, "%Y-%m-%d %H:%M:%S")
    # # 转换成时间戳
    # return int(time.mktime(timeArray))
    d = datetime.datetime.strptime(str(time___), "%Y-%m-%d %H:%M:%S")
    t = d.timetuple()
    return int(time.mktime(t))


def timestamp_to_date(t__):
    timeStamp = int(t__)
    if timeStamp > 3000000000:
        timeArray = time.localtime(int(timeStamp) // 1000)
    else:
        timeArray = time.localtime(int(timeStamp))
    return datetime.date(timeArray.tm_year, timeArray.tm_mon, timeArray.tm_mday)


def time_to_date(timeArray):
    return timestamp_to_date(time_to_timestamp(timeArray))
