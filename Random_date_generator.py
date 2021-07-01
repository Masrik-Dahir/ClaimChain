import random
import time
import datetime

def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


def today():
    current_time = datetime.datetime.now()
    return str(current_time.month) + "/" +str(current_time.day) + "/" + str(current_time.year)
