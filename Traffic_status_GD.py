#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:Traffic_status_GD.py
@Time:2020/09/08 20:16:53
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:获取高德地图交通态势数据
@由于高德地图封闭了个人key获取交通态势，所以只能通过爬取中间网站来获取
http://www.guihuayun.com/tools.php?id=22
@本程序仅为自己研究学习用途，不做其他商业用途
'''

import requests
import time
import json
from fake_useragent import UserAgent
import math
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def get_traffic_status():
    re_url= 'http://in5.cn/guihuayun/get_status.php'
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '70',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'in5.cn',
        'Origin': 'http://in5.cn',
        'Referer': 'http://in5.cn/guihuayun/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    data = {
        'gaode_key': '31ba74be178044d87c0e40a48d20d160', # 高德开发者账号
        'get_xy': '120.868456,30.017848' # 范围中心点坐标 https://mp.weixin.qq.com/s?__biz=MzIxMDgxODM0Mw==&mid=2247485583&idx=1&sn=acbbb2d3d7a3fc2f3a9bf8062134cf12&chksm=975f8cc7a02805d194f2ea08d0e5b827e3446e4383c95073f59145c31e4ac026d73d3bc80c84&mpshare=1&scene=23&srcid=&sharer_sharetime=1589265635663&sharer_shareid=ee9139f255adf3201f2f593ba2b370c9#rd
    }
    resp = requests.post(re_url, data=data, headers=headers)
    resp.encoding = resp.apparent_encoding
    html = resp.text
    bf=BeautifulSoup(html)
    load_url=bf.a['href']
    file_name=load_url.split('/')[-1]
    local_path='C:/Users/a6540/Desktop/Traffic_Status_GD/'+file_name
    urlretrieve(load_url,local_path)
if __name__ == "__main__":
    get_traffic_status()