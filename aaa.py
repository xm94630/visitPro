# -*- coding: UTF-8 -*-

# browser.get("http://httpbin.org/ip")
# browser.set_window_size(1400, 900)
# print(browser.page_source)

# 114.113.126.86:80   #上海
# 222.221.11.119:3218 #云南昆明
# 61.138.33.20:808    #七里河
# 115.151.2.154:808   #江西宜春

import time
import random
import re
from selenium import webdriver
from fake_useragent import UserAgent



options = {
    'proxyServer':"125.70.13.77:8080", #代理服务器
    'myWeb':"http://www.jiaoda7.com",  #入口页面
    'reg':r".*jiaoda.*",               #要访问的子链接的关键词（正则）
    'sonPageRange':[1,3],              #子页面访问数量可选范围
    'timeRange':[3,5],                 #页面访问的时间可选范围
}


def xxx(options):

    #设置
    proxyServer  = options['proxyServer']
    myWeb        = options['myWeb']
    reg          = options['reg']
    sonPageRange = options['sonPageRange']
    timeRange    = options['timeRange']

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-agent="' + UserAgent().random + '"')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--proxy-server=http://"+proxyServer)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    
    # 访问入口页面
    visitTime = random.randint(timeRange[0],timeRange[1])
    browser.get(myWeb)
    print '[main page]'+str(visitTime)+'s '+myWeb
    time.sleep(visitTime)

    # 访问子页面
    def visitSonPage(total):
        visitTime = random.randint(timeRange[0],timeRange[1])
        linksElements = browser.find_elements_by_tag_name('a')
        linksArr = [];
        #提取链接
        for ele in linksElements:
            linkUrl = ele.get_attribute('href')
            #正则过滤
            matchObj = re.match(reg,linkUrl)
            if matchObj:
                #print linkUrl
                linksArr.append(linkUrl);

        #访问下一个页面
        if  len(linksArr)==0:
            #如果没有链接则继续访问入口页面
            browser.get(myWeb)
        else:
            #随机选择一个链接
            r = random.randint(0, len(linksArr)-1)
            sonLink = linksArr[r]
            browser.get(sonLink)
            print '[son page]'+str(visitTime)+'s '+sonLink
            

        time.sleep(visitTime)

        total = total-1;
        if total>0:
            visitSonPage(total);

    sonPageN = random.randint(sonPageRange[0],sonPageRange[1])
    # 递归访问子页面
    visitSonPage(sonPageN);


    print('页面关闭')
    browser.close();
    time.sleep(10)
    print('程序退出')
    browser.quit()

xxx(options);