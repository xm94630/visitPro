# -*- coding:utf8 -*-

import urllib
import socket
import sys
import re

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://httpbin.org/ip"
#xm:注意这个超时设置是这样子写的，单位是秒
socket.setdefaulttimeout(10)
# 从命令行获取代理ip
try:
    proxyIp =  sys.argv[1]
except:
    proxyIp = False

if proxyIp:
    print '【单独验证】'
    proxy={"http":"http://"+proxyIp}
    try:
        res = urllib.urlopen(url,proxies=proxy)
        if res.code==200:
            html = res.read()
            if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',html):
                print html
            else:
                #print html
                print 'sb!!' 
        else:
            print '[code]' + str(res.code)
    except Exception,e:
        print 'error!!'
        print e

else:
    print '【全体验证】'
    inf = open("ip1.txt")    
    lines = inf.readlines()
    proxys = []
    for i in range(0,len(lines)):
        proxy_host = "http://" + lines[i]
        proxy_temp = {"http":proxy_host}
        proxys.append(proxy_temp)

    # 将可用ip写入valid_ip.txt
    ouf = open("ip2.txt", "a+")

    len = len(proxys)
    for i in range(0,len):
        myIp = proxys[i]['http'][7:]
        print '---------------------------------------------------------------------------------('+str(i)+'/'+str(len)+')';
        print myIp.strip() #xm:这个myIp后面有个空行，我把它去了
        try:
            res = urllib.urlopen(url,proxies=proxys[i])
            if res.code==200:
                html = res.read()
                if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',html):
                    print 'success!'
                    ouf.write(myIp)
                else:
                    #print html
                    print 'sb!!' 
            else:
                print '[code]' + str(res.code)

        except Exception,e:
            print e
            continue
