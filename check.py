# -*- coding:utf8 -*-

import urllib
import socket
import sys
import re

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://httpbin.org/ip"
#url = "http://www.jiaoda7.com"
#xm:注意这个超时设置是这样子写的，单位是秒
socket.setdefaulttimeout(3)
# 从命令行获取代理ip
try:
    proxyIp =  sys.argv[1]
except:
    proxyIp = False

if proxyIp:
    print '【单独验证】'
    proxys=[{"http":"http://"+proxyIp}]
    i=0
    try:
        res = urllib.urlopen(url,proxies=proxys[i])
        html = res.read()
        print(html)
        if res.code==200:
            # 如果html中包含"origin"，则成功（因为有的代理ip居然返回“有道”的html！）
            arr = re.findall(r'"origin"',html)
            if len(arr)>0:
                print '--------------------------'
                print "[xm]本ip可以使用"
            else:
                print '[xm]搞笑吧！' 
        else:
            print '[xm]返回码为' + str(res.code)
    except Exception,e:
        print '[xm]请求发生问题！'
        print e

else:
    print '【全体验证】'
    total = 0;
    inf = open("ip1.txt")    
    lines = inf.readlines()
    proxys = []
    for i in range(0,len(lines)):
        proxy_host = "http://" + lines[i]
        proxy_temp = {"http":proxy_host}
        proxys.append(proxy_temp)

    # 将可用ip写入ip2.txt
    ouf = open("ip2.txt", "a+")
    ouf = open("ip2.txt", "r+")

    #神坑千万别那么写了！len是关键词
    #len = len(proxys)
    length = len(proxys);

    for i in range(0,length):
        myIp = proxys[i]['http'][7:]
        print '---------------------------------------------------------------------------------('+str(i)+'/'+str(length)+') 已有可用:'+str(total);
        print myIp.strip() #xm:这个myIp后面有个空行，我把它去了
        try:
            res = urllib.urlopen(url,proxies=proxys[i])
            html = res.read()
            #print(html)
            if res.code==200:
                # 如果html中包含"origin"，则成功（因为有的代理ip居然返回“有道”的html！）
                arr = re.findall(r'"origin"',html)
                if len(arr)>0:
                    print "[xm]本ip可以使用"
                    print '--------------------------写入文件'
                    ouf.write(myIp)
                    total += 1;
                else:
                    print '[xm]搞笑吧！' 
            else:
                print '[xm]返回码为' + str(res.code)
        except Exception,e:
            print '[xm]请求发生问题！'
            print e
