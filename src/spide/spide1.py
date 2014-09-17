# coding = utf-8
# -*- coding:utf-8 -*-

import urllib.request

url = "http://w3b.ibm.com/"
html = urllib.request.urlopen(url).read()
print(html)