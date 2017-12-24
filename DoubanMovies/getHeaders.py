#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2017/12/10
 @ Author: songpo.zhang
 @ Target:
"""
def proxypool(num):
    n = 1
    #os.chdir(r'/Users/apple888/PycharmProjects/proxy IP')
    fp = open('host.txt', 'r')
    proxys = list()
    ips = fp.readlines()
    while n<num:
        for p in ips:
            ip = p.strip('\n').split('\t')
            proxy = 'https://' + ip[0] + ':' + ip[1]
            proxies = {'http': proxy}
            #print(proxies)
            proxys.append(proxies)
            n+=1
    return proxys


def getCookie():
    cookie_list = [
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490333053.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334307.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334337.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334547.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334576.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=-2pPxf20f-A; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1490334617%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6-V4k_jr0yx56VVthcFdBh1dsEw-fM_VidsCvjvnZDu%26wd%3D%26eqid%3Ddb5853390004c0f20000000258d4b38f%22%5D; _pk_id.100001.8cb4=cd9595388e4feada.1490334617.1.1490334617.1490334617.; _pk_ses.100001.8cb4=*; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.1.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334690.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334724.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334758.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334785.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        '__utmc=30149280; ll=118237; bid=BpRkUyl8224; __utma=30149280.2117353028.1490334856.1490334856.1490334856.1; __utmb=30149280.1.10.1490334856; __utmz=30149280.1490334856.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _vwo_uuid_v2=3DE3A5524E7D8D0F707D6C9AEB95A43B|da39a7ae190f4c2de62535e9911c57a6; __utma=223695111.747047863.1490334857.1490334857.1490334857.1; __utmb=223695111.0.10.1490334857; __utmc=223695111; __utmz=223695111.1490334857.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334858%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=0025ca3c57b38c6f.1490334858.1.1490334858.1490334858.; _pk_ses.100001.4cf6=*',
        '__utmc=30149280; ll=118237; bid=BpRkUyl8224; __utma=30149280.2117353028.1490334856.1490334856.1490334856.1; __utmb=30149280.1.10.1490334856; __utmz=30149280.1490334856.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _vwo_uuid_v2=3DE3A5524E7D8D0F707D6C9AEB95A43B|da39a7ae190f4c2de62535e9911c57a6; __utma=223695111.747047863.1490334857.1490334857.1490334857.1; __utmb=223695111.0.10.1490334857; __utmc=223695111; __utmz=223695111.1490334857.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334858%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=0025ca3c57b38c6f.1490334858.1.1490334918.1490334858.; _pk_ses.100001.4cf6=*']

    return cookie_list

def getUserAgent():
    UA_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
               "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
               "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
               "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
               "Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 Mobile/14B100 Safari/602.1",
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
               "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
               "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"]
    return UA_list
