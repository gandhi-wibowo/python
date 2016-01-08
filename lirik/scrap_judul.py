#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

url = "http://www.wowkeren.com/seleb/peterpan/lirik.html"
base_url = "http://www.wowkeren.com"

def CariJudul(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page,'lxml')
    link = [x.findAll("a") for x in soup.findAll("div",{"id":"IsiUmum"})]
    for judul in range(len(link)):
        if link[judul]:
            for j, i in enumerate(link[judul]):
                print j,i.text
                data=[base_url+i['href']]
                return data

CariJudul(url)
