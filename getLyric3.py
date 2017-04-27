# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import re
import json
import getMusicList as gml
import sys
import os
import shutil
import ast
word_stat = {}

try:
    os.mkdir("lyric")
    os.mkdir("lyric/low-hearted")
    os.mkdir("lyric/high-hearted")
except OSError as err:
    print(format(err))
    pass

def getlyricfromurl(sid, c, counts, fails, flist):
    hm = 'http://music.163.com/api/song/lyric?os=pc&' + sid +'&lv=-1&kv=-1&tv=-1'
    data_json = gml.gethtml(hm)
    data = json.loads(data_json)
    reg = r'[^0-9\[\]\.\:]'
    string = re.compile(reg)
    lyricname = ""
    ger = ["low-hearted","high-hearted"]
    gtags = ["(1,0)\n\n", "(0,1)\n\n"]
    gna = ger[c]
    gtag = gtags[c]
    try:
        st = data["lrc"]["lyric"]
        # print st
        lyriclist = re.findall(string, st)
        # print 1
        if 'klyric' in data and "lyric" in data['klyric'] and not data['klyric']["lyric"] is None:
                lyricname = data['klyric']["lyric"]
                end = lyricname.index("]")
                lyricname = lyricname[4:end]
        # print 2
        str_lrc = ','.join(lyriclist)
        fn = 'lyric/' + gna + '/' + sid[3:] + '.txt'
        flist.append(fn)
        # print 3
        with open(fn, 'w+') as file:
            file.write(gtag)
            file.write(lyricname + '\n')
            file.write(str_lrc.replace(',', ''))
            file.close()
        counts[c] += 1
    except:
        fails[c] += 1
        #print hm
        pass
    #print counts[c],fails[c]

if __name__ == '__main__':
    pl = [['35489748','759311','28359012','519341391','489669263','80929718','25937065','102232330','125563756','62445076','46661467','10775191','2182552','551581313',\
    '10775191','361197245','470216068','6491553','157500452','71805816','2206331','24940553','161232468','94702013','46771768','65450384','64047958','41672586','68263767','448634766','23555969','45637271'],\
    ['73689168','545780979','361892699','633141677','57656511','26517509','369923169','568165922','633322322','690576372','496557907','28357911','537413400','147257106','518398846','111624864','522429673',\
    '76786343','487674809','39858559','374235566','35765708','33591856','544387381','160290354']]
    cset = set([])
    counts = [0,0]
    fails = [0,0]
    idlist = []
    for i in range(2):
        l = pl[i]
        for lid in l:
            html = gml.gethtml("http://music.163.com/playlist?id=" + lid)
            musiclist = gml.getmusic(html)
            for key in musiclist:
                if not key in cset:
                    cset.add(key)
                    #counts[i] += 1
                    getlyricfromurl(key, i, counts, fails, idlist)
                    print("list id is " + lid + " count is " + str(counts[i]))
                    if counts[i] > 2776:
                        break
            if counts[i] > 2776:
                break

    file = open("pathlist.txt", "w+")
    json.dump([idlist], file)
    file.close()
    print(counts)

def main():
    pass
