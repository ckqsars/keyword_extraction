#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqcins@gmail.com>
#

import keyword_extraction
import numpy as np

def read_input(fd,delimiter):
    datalist = []
    for obj in fd:
        datalist.append(obj.strip().split(delimiter))
        # words = obj.strip().split(' ')
        # for word in words:
        #     datalist.append(word)
    return datalist

def read_input1(fd,delimiter):
    datalist = []
    for obj in fd:
        datalist.append(obj.strip())
    return datalist


def main():

    data_path = '../data/keyword-extraction-datasets-master/keyword-extraction-datasets-master/fao30/documents'
    stop_word_file = '../data/stopword.txt'
    fr_stop_word = open(stop_word_file)

    stop_word_list = read_input1(fr_stop_word, delimiter=' ')
    keyword = keyword_extraction.keyword_extraction(limit_sen_num = 3, time_window = 6, data_path = data_path
                                                    , stop_word_list = stop_word_list)
#     datafile = '../data/keyword-extraction-datasets-master/keyword-extraction-datasets-master/fao30/documents/a0011e00.txt'

#     fr = open(datafile)

#     sentencelist = read_input(fr, delimiter=' ')
#     print len(sentencelist)

# #
# #
#     sentencelist = keyword.InitWordCoMatrix(stop_word_list=stop_word_list, sentencelist= sentencelist,)
#     for sentence in sentencelist:
#         matrix = keyword.Construct_Matrix(sentence)
#         print matrix
#         break
if __name__ == '__main__':
    main()