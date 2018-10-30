# -*- coding:utf8 -*-

import urllib2
import re
import time
import random


# 代理 如果自己的ip、被封了，就可以用代理（我自己电脑的上一个ip用了一次就不行了，好在是动态的ip隔一段时间就更新了）
# 这个 urllib2 的代理，写法有点麻烦...
# proxies={"http":"113.16.160.101:8118"} 
# proxy_s = urllib2.ProxyHandler(proxies)
# opener = urllib2.build_opener(proxy_s)
# urllib2.install_opener(opener)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Hosts': 'hm.baidu.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}

# 测试ip
# url = 'http://httpbin.org/ip'
# req = urllib2.Request(url=url,headers=headers)
# res = urllib2.urlopen(req).read()
# print res

# # 指定爬取范围（这里是第1~1000页）
for i in range(1,1000):

    url = 'http://www.xicidaili.com/nn/' + str(i)
    req = urllib2.Request(url=url,headers=headers)
    res = urllib2.urlopen(req).read()

    # 提取ip和端口
    ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", res, re.S)

    # 将提取的ip和端口写入文件
    f = open("ip.txt","a+")
    for li in ip_list:
        ip = li[0] + ':' + li[1] + '\n'
        print ip
        f.write(ip)

    #访问的时间间隔随机一点
    n = random.randint(4,8)
    time.sleep(n)       # 每爬取一页暂停两秒