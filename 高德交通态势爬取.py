# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:32:29 2019

@author: hp
"""

import requests
import time



url='https://restapi.amap.com/v3/traffic/status/rectangle?key=21e4500b5ac591e0cd9b0abcc7e2a738&extensions=all&rectangle=116.351147,39.966309;116.357134,39.968727'
f=open('C:/Users/user/Desktop/高德交通态势爬取/'+time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())+'.csv','w')
f.seek(0)
    
f.write('道路名,路况,速度,编号,经度,纬度\n')

r=requests.get(url)
s=r.json()           
print(s)
x=[]      
if s['info']=='OK':
               
               
    a=s["trafficinfo"]["roads"]#列表a,由字典组成
                
    num1=0

    for i in range(len(a)):
        
                       
        a[i].get("polyline")
        s2=a[i].get("polyline")
        s3=str(s2).split(";")
        num1=num1+1
        for j in range(len(s3)):
            
                           
            s4=s3[j].split(",")
            a[i].get("speed")
            if len(s4)==2:
                
                               
                lst=[a[i]["name"],a[i].get("status"),a[i].get("speed"),i,s4[0],s4[1]]
                #print(lst)
                        
                f.writelines([str(lst[0]),',',str(lst[1]),',',str(lst[2]),',',str(lst[3]),',',str(lst[4]),',',str(lst[5]),'\n'])
                
                           
            else:
                    
                print('未知错误')
else:
               
    print('未知错误')
                
                
                    
f.close()

print('finishedTime:'+time.ctime())