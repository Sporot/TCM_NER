#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : utils.py
# @Author: Song bing yan
# @Date  : 2020/3/29
# @Des   : 对维基百科处理的工具函数

import TCM_corpus.GlobalParament as GlobalParament

import re

def delete_r_n(line):
    """
    去掉空行等
    :param line:
    :return:
    """
    return line.replace('\r', '').replace('\n', '').strip()


def get_tag_word(word_dir):
    """
    读取分好词
    :param word_dir:
    :return:返回列表
    """
    word_tag = []

    with open(word_dir, 'r', encoding='utf-8') as f:
        for line in f:
            line = delete_r_n(line)
            word_list = line.split(' ')
            # print(word_list)
            for word in word_list:
                word_tag.append(word)
    word_tag = set(word_tag)
    return word_tag


def char_cut(content):
    """
    按单字进行分隔
    :param content:
    :return: 单字列表
    """
    char_list = []

    if content is not None and content != '':
        for char in content:
                char_list.append(char)
    return char_list

def bichar_cut(content):
    """
    按双字分句
    :param line:
    :return:
    """
    bichar_list=[]

    mac1 = ''
    if content is not None and content !='':
        for i,bichar in enumerate(content):
                if i != 0 and i % 2 == 0:
                    mac1 = mac1 + '-' + content[i]
                else:
                    mac1 = mac1 + content[i]
        for word in mac1.split('-'):
            if len(word)==2:
                bichar_list.append(word)
            else:
                word=word+'。'
                bichar_list.append(word)
    return bichar_list

def clear_char_from_vocab(char_list, vocab):
    """
    清除不在词表中的字
    :param char_list:
    :param vocab:
    :return:
    """
    new_char_list = []

    for char in char_list:
        if char in vocab:
            new_char_list.append(char)

    return new_char_list


def text_to_char(text_dir, text_char_dir):
    """
    按单字将维基百科进行分隔
    :param text_dir: 维基百科原文
    :param text_char_dir: 处理后的单字文本
    :return: 单字句
    """
    sentences = []
    count = 0;

    f_writer = open(text_char_dir, 'w', encoding=GlobalParament.encoding)
    with open(text_dir, 'r', encoding=GlobalParament.encoding) as f_reader:
        for line in f_reader:
            line = delete_r_n(line)
            char_list = char_cut(line)
            if len(char_list) > 0:
                sentences.append(char_list)
                f_writer.write(" ".join(char_list) + '\n')
                f_writer.flush()
            count = count + 1
            print(count)
    f_writer.close()
    return sentences

def text_to_bichar(text_dir,text_bichar_dir):
    """
    按两个字对维基百科进行分隔
    :param text_dir: 维基百科原文
    :param text_bichar_dir: 处理后的双子文本
    :return: 双字句
    """
    sentences=[]
    count=0

    f_write=open(text_bichar_dir,'w',encoding=GlobalParament.encoding)
    with open(text_dir,'r',encoding=GlobalParament.encoding) as f_reader:
        for line in f_reader:
            line=delete_r_n(line)
            bichar_list=bichar_cut(line)
            if len(bichar_list) >0:
                sentences.append(bichar_list)
                f_write.write(" ".join(bichar_list)+'\n')
                f_write.flush()
            count=count+1
            print(count)
    f_write.close()
    return sentences

# 加载处理后的文本数据
def load_traintext(text_afterprocess_alldata):
    sentences = []

    with open(text_afterprocess_alldata, 'r', encoding=GlobalParament.encoding) as f:
        for line in f:
            line = delete_r_n(line)
            char_list = line.split(' ')
            sentences.append(char_list)
    return sentences


# 将样本集合成一个文档
def sample_concat(sample_dir, sample_concat_dir):
    sentences = []
    f_writer = open(sample_concat_dir, 'w', encoding=GlobalParament.encoding)

    with open(sample_dir, 'r', encoding=GlobalParament.encoding) as f_reader:
        for line in f_reader:
            # line=delete_r_n(line)
            if len(line) > 0:
                char = line[0]
                print(type(char))
                sentences.append(char)
                f_writer.write(char)
    return sentences


# def dictionary_contact(dictionary_dir, dictionary_concat_dir):
#     sentences = []
#     count = 0
#     f_writer = open(dictionary_concat_dir, 'w', encoding=GlobalParament.encoding)
#
#     with open(dictionary_dir, 'r', encoding=GlobalParament.encoding) as f_reader:
#         for line in f_reader:
#             count = count + 1
#             line = delete_r_n(line)
#             if len(line) > 0:
#                 if count == 20:
#                     f_writer.write(line + '\n')
#                     count = 0
#                 sentences.append(line)
#                 f_writer.write(line + ',')
#     return sentences

def reduce_first(readp,writep):
    f_write = open(writep,'a',encoding='utf-8')
    f_read = open(readp,'r',encoding='utf-8')
    lines = f_read.readlines()
    print(lines[0])
    print(len(lines))

    num =0
    for i in range(3,len(lines)):
        if len(lines[i].split())==301:
            num =num+1
            f_write.write(lines[i])
    print(num)
    # for i in range(3, 26757):
    #     f_write.write(lines[i])
    #
    # for i in range(26758,)

    return

if __name__ == '__main__':
    #text_to_char(GlobalParament.text_dir,GlobalParament.text_to_char_dir)
    # bichar_list=bichar_cut('我今天不是很高，房fjasdjfakjfka放假啊士大夫静安寺搭街坊卡拉，就搭街坊卡拉，的发生分解ask《魔法师的法术抵抗')
    # print(bichar_list)
    #text_to_bichar('../data/book_all.txt','../data/data_all_after_bichar.txt')
    reduce_first('vec/char_300.txt','vec/char_300_em.txt')



