# -*-coding:utf-8-*-
from __future__ import unicode_literals
import urllib.request
import sys
import re


def gethtml(url):
    with urllib.request.urlopen(url) as url_fp:
        html= url_fp.read().decode('utf-8')
        return html


def getmusic(html):
    reg = r'href="/song\?id=[0-9]{0,9}"'

    musicre = re.compile(reg)
    musiclist_temp = re.findall(musicre, html)
    musiclist = []
    for item in musiclist_temp:
        musiclist.append(item[12:-1])
    return musiclist
