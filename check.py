# -*- coding:utf8 -*-

import urllib
import socket

#xm:注意这个超时设置是这样子写的，单位是秒
socket.setdefaulttimeout(3)

inf = open("ip1.txt")    
lines = inf.readlines()
proxys = []
for i in range(0,len(lines)):
    proxy_host = "http://" + lines[i]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://httpbin.org/ip"
# 将可用ip写入valid_ip.txt
ouf = open("ip2.txt", "a+")


len = len(proxys)
for i in range(0,len):
    myIp = proxys[i]['http'][7:]
    print '---------------------------------------------------------------------------------('+str(i)+'/'+str(len)+')';
    print myIp.strip() #xm:这个myIp后面有个空行，我把它去了
    try:
        res = urllib.urlopen(url,proxies=proxys[i]).read()
        print 'success!'
        ouf.write(myIp)
    except Exception,e:
        print e
        continue
1