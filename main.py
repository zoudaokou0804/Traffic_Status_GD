#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:main.py
@Time:2020/09/08 21:07:43
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:实现定时间间隔自动采集
'''
from datetime import datetime, time
import time as ti
from threading import Timer
from Traffic_status_GD import get_traffic_status
# 设置5min自动运行程序采集
def auto_crawl_tf_status_gd(time_periods):
    print('自动化采集中.......')
    NIGHT_START = time(6, 0) # 表示0:14
    NIGHT_END = time(18, 0)   #表示0:59
    current_time = datetime.now().time()
    while NIGHT_START <= current_time <= NIGHT_END:
        print('hello')
        get_traffic_status()
        current_time = datetime.now().time()
        left_time=(int(NIGHT_END.hour)-int(current_time.hour))*3600+(int(NIGHT_END.minute)-int(current_time.minute))*60+(int(NIGHT_END.second)-int(current_time.second))*1
        if left_time <= time_periods:
            break
        else:
            ti.sleep(time_periods)
            current_time = datetime.now().time()
    print('数据采集完毕.......')
if __name__ == "__main__":
    time_periods=10
    auto_crawl_tf_status_gd(time_periods)