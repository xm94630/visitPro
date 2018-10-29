# -*- coding: UTF-8 -*-

# browser.get("http://httpbin.org/ip")
# browser.set_window_size(1400, 900)
# print(browser.page_source)

# 125.70.13.77:8080   #成都
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
    #'proxyServer':"125.70.13.77:8080",  #代理服务器 上海
    #'proxyServer':"222.217.68.51:54355",  #代理服务器 柳州
    'proxyServer':"60.191.201.38:45461",  #代理服务器
    'myWeb':"http://www.jiaoda7.com",   #入口页面
    'reg':r".*jiaoda.*",               #要访问的子链接的关键词（正则）
    'ignoreReg':r".*jiaoda3.*",        #不要访问的子链接的关键词（正则） 因为，这个程序不能遇到有alert的，我的交大3就有一个...它就崩溃了，要排除
    'sonPageRange':[0,1],              #子页面访问数量可选范围
    'timeRange':[1,5],                 #页面访问的时间可选范围
    'keywords':[                       #关键词
        '交大群侠传',
        '交大群侠传2',
        '交大群侠传3',
        '交大群侠传官网',
        '交大群侠传 官网',
        '交大群侠传2官网',
        '交大群侠传2黄金版',
        '交大群侠传2 黄金版',
        '交大群侠传黄金版',
        '交大群侠传2 官网',
        '交大群侠传2攻略',
        '交大群侠传攻略',
    ]
}


def run(options):

    #设置
    proxyServer  = options['proxyServer']
    myWeb        = options['myWeb']
    reg          = options['reg']
    ignoreReg    = options['ignoreReg']
    sonPageRange = options['sonPageRange']
    timeRange    = options['timeRange']
    keywords     = options['keywords']

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-agent="' + UserAgent().random + '"')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--proxy-server=http://"+proxyServer)
    chrome_options.add_argument('--referer=https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%BA%A4%E5%A4%A7%E7%BE%A4%E4%BE%A0%E4%BC%A0&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E4%25BA%25A4%25E5%25A4%25A7%25E7%25BE%25A4%25E4%25BE%25A0%25E4%25BC%25A0&rsv_pq=95213b240001aa52&rsv_t=33cb91U2x6b4xvu5RimAjU0ZSxGPli3rLJk%2BWZphe5QdE3oGishm1Yfheqs&rqlang=cn&rsv_enter=1&sug=selenium&inputT=370&rsv_sug3=79&rsv_sug1=77&rsv_sug7=100&rsv_sug2=0&rsv_sug4=612')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    #从百度搜索进去    
    #本来这个可以通过referer的设置就能搞定，不过官方处于安全不让设置这个，所以这里就麻烦点。
    n = random.randint(0,len(keywords)-1)
    keyword = keywords[n]
    browser.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='+keyword+'&oq=%25E4%25BA%25A4%25E5%25A4%25A7%25E7%25BE%25A4%25E4%25BE%25A0%25E4%25BC%25A0&rsv_pq=894d93200002bc5f&rsv_t=9313spxQN1fbQoCjinuoWUdmCFGXtzOOsiPPSKyDzrZd3zI6kmhUWBF0V7U&rqlang=cn&rsv_enter=0')
    print('百度搜索关键词：'+keyword)

    try:
        #要是在百度首页能找到我的，就点进去，找不到，我也懒得翻页处理了...直接跳转到主页
        #print browser.find_element_by_partial_link_text("jiaoda7.com").get_attribute('href')
        browser.find_element_by_partial_link_text("jiaoda7.com").click();
        print('在首页查询成功！')
        time.sleep(3)
    except:
        #不处理
        print('首页查询失败，不再处理，跳过百度搜索部分')
    
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
            if re.match(reg,linkUrl):
                if re.match(ignoreReg,linkUrl):
                    pass
                else:
                    print linkUrl
                    linksArr.append(linkUrl)
                
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

    time.sleep(10)
    print('页面关闭')
    browser.close();
    time.sleep(10)
    print('程序退出')
    browser.quit()

run(options);