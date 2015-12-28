#!/usr/bin/python

import re
import sys
import urllib2
from bs4 import BeautifulSoup


'''
cari daftar lagu berdasarkan nama grup band dari link www.wowkeren.com
'''
if len(sys.argv) <2:
    print "Usage : "+ sys.argv[0] +" Group Band"
    print "Example :"+ sys.argv[0] +" peterpan"

band = sys.argv[1]
url = 'http://www.wowkeren.com/seleb/'+band+'/lirik.html'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')
data = [x.findAll("a") for x in soup.findAll("div",{"id":"IsiUmum"})]
for dl in range(len(data)):
    if data[dl]:
        for i in data[dl]:
            print i['href']+ " => "+ i.text
