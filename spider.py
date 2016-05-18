# -*- coding: utf-8 -*-
#
#---------------------------------------------------
#   爬虫：hustoj_spider
#   作者: helica
#   日期: 2015-8-12
#   语言: py2
#
#
#---------------------------------------------------

import urllib
import urllib2
import re
import cookielib

global cookie
cookie = cookielib.CookieJar()

def login():
    global cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    
    postdata = urllib.urlencode({
        'username':'helica',
        'password':''
    })

    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

    opener.addheaders = [headers]

    req = urllib2.Request(
        url = 'http://acm.hust.edu.cn/vjudge/user/login.action',
        data = postdata
    )

    result = opener.open(req)


    return result.read()

def getInfo():
    global cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheaders = [headers]

    req = urllib2.Request(url = 'http://acm.hust.edu.cn/vjudge/contest/view.action?cid=66989#overview')

    result = opener.open(req)
    return result.read()

def SubCode():
    global cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheaders = [headers]

    submitdata = urllib.urlencode({
        'cid':'79121',
        'num':'C',
        'language':'3',
        'isOpen':'0',
        'source':'Ly9sZXQgbWUgZG8gYSB0ZXN0IHRvIGZpbmQgdGhlIHVybCBvZiB0aGUgYWRkIGkgc3ViIG15IGNvZGUKLy9pIHdhbnQgbWFrZSBhIHNwaWRlciBmb3IgbXkgdmltCi8vc28gdGhhdCBpIGNhbiBzdWJtaXQgY29kZSB2aWEgbXkgZWRpdG9yIFhE'
    })

    req = urllib2.Request(
        url = 'http://acm.hust.edu.cn/vjudge/contest/submit.action',
        data = submitdata
        )
    
    result = opener.open(req)
    
    return result.read()

def getStatus():
    global cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheaders = [headers]



print login()
#print getInfo()
print SubCode()
