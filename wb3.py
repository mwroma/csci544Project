# -*- coding: utf-8 -*-
import jieba
import os
import shutil
import re
import pickle
from hanziconv import HanziConv
import sys



non_lyric_indicators = ['作曲','作词', '制作人', '编曲', '录音', '和音','和声指导','美工','文案','鸣谢',\
'演唱','——记', '缩混', '封面', 'pv', '歌名题字', '念白', 'by', 'ti', 'ar', 'al', 'offset', '曲编', '二胡']
special_chars = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：\-【】 ；》《のテ·マ]+"


def load_stop_word():
    with open('stop_words.txt', encoding="utf-8") as fp:
        l = fp.read()
        stwords = l.split("\n")
        return set(stwords)

def clean_line(line):
    line = line.strip()
    for indicator in non_lyric_indicators:
        if line.startswith(indicator):
            return ''
    line = re.sub(r'[0-9a-zA-Z]', '', line)
    line = re.sub(special_chars, '', line)
    line = HanziConv.toSimplified(line)
    return line

def parse_label(line):
    line = line[1:-1]
    result = line.split(',')
    result = list(map(int, result))
    return result

def build_word_set(rootDir, stop_words, word_set):
    list_dirs = os.walk(rootDir)
    print (list_dirs)
    for root, dirs, files in list_dirs:
        for f in files:
            words = []
            label = []
            file_path = os.path.join(root, f)
            if ".DS_Store"  in file_path:
                continue
            with open(file_path, 'r', encoding="utf-8") as fp:
                lines = fp.read().split('\n')
                label = parse_label(lines[0])
                for line in lines[2:]:
                    line = clean_line(line)
                    if line:
                        line_words = jieba.cut(line, cut_all=False)
                        for word in line_words:
                            if word not in stop_words:
                                word_set.add(word)
                                words.append(word)
            result = {'word_list':words, 'label1':label}
            temp_file_path = os.path.join('temp', f)
            with open(temp_file_path, 'wb+') as fp:
                pickle.dump(result, fp, protocol=pickle.HIGHEST_PROTOCOL)
    return word_set

def build_word_bag(word_dic):
    length = len(word_dic)
    list_dirs = os.walk('temp')
    for root, dirs, files in list_dirs:
        for f in files:
            word_bag = [0] * length
            file_path = os.path.join(root, f)
            with open(file_path, 'rb') as fp:
                unserialized_data = pickle.load(fp)
                word_list = unserialized_data['word_list']
                for word in word_list:
                    word_bag[word_dic[word]] += 1;
            result = {"word_bag":word_bag, "label1":unserialized_data["label1"]}
            bag_path = os.path.join("bags", f)
            with open(bag_path, 'wb+') as fp:
                pickle.dump(result, fp, protocol=pickle.HIGHEST_PROTOCOL)


def dir_prepare():
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    if os.path.exists('bags'):
        shutil.rmtree('bags')
    os.mkdir('temp')
    os.mkdir('bags')

def main():
    dir_prepare()
    stop_words = load_stop_word()
    word_set = build_word_set('lyric', stop_words, set())
    word_list = list(word_set)
    word_dic = {k: v for v, k in enumerate(word_list)}
    build_word_bag(word_dic)



if __name__ == "__main__":main()
