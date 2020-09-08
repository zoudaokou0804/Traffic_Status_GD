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
from threading import Timer
from Traffic_status_GD import get_traffic_status
# 设置5min自动运行程序采集
def auto_crawl_tf_status_gd(time_periods):
    print('自动化采集中.......')
    NIGHT_START = time(20, 30)
    NIGHT_END = time(2, 30)
    current_time = datetime.now().time()
    if NIGHT_START <= current_time <= NIGHT_END:
        print('hello')
if __name__ == "__main__":
    time_periods=10
    auto_crawl_tf_status_gd(time_periods)