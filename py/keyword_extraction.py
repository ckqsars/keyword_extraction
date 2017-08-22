#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2017 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqcins@gmail.com>
#

import re
import numpy as np
import os

class keyword_extraction(object):
    def __init__(self, limit_sen_num, time_window, data_path, stop_word_list):
        self.limit_sen_num = limit_sen_num
        self.time_window = time_window
        self.stop_word_list = stop_word_list
        self.wordlist = self.Construct_wordlist(data_path)
        print len(self.wordlist)






    def InitWordCoMatrix(self,  stop_word_list, sentencelist):
        self.sentencelist = self.RM_NoneSenceSentence(sentencelist)


        for i in range(len(self.sentencelist)):
            self.sentencelist[i] = self.rm_punctuation(self.sentencelist[i])

        print self.sentencelist

        self.rm_stop_word(stop_word_list)
        # self.wordlist = self.Construct_wordlist()

        return self.sentencelist

    def RM_NoneSenceSentence(self, sentencelist):
        NewSentenclist = []
        for sentence in sentencelist:
            if len(sentence) > self.limit_sen_num:
                NewSentenclist.append(sentence)


        return NewSentenclist

    def rm_punctuation(self, words):

        self.parrtern = re.compile('\W')
        for i in range(len(words)):
            words[i] = self.parrtern.sub('',words[i])
            words[i] = words[i].lower()

        return words


    def rm_stop_word(self, words, stop_word_list):
        # for i in range(len(self.sentencelist)):
        #     delet_list = []
        #     for j in range(len(self.sentencelist[i])):
        #         if self.sentencelist[i][j] in stop_word_list:
        #             delet_list.append(self.sentencelist[i][j])
        #
        #     for word in delet_list:
        #         del self.sentencelist[i][self.sentencelist[i].index(word)]
        for word in words:
            if word in stop_word_list:
                words.remove(word)

        return words


    def Construct_wordlist(self, data_path):
        wordlist = []
        delimiter =' '
        t = 0
        for filename in os.listdir(data_path):
            fr = open(data_path+'/'+filename)
            for obj in fr:
                try:
                    words = obj.strip().split(delimiter)
                    words = self.rm_stop_word(self.rm_punctuation(words), self.stop_word_list)
                    for word in words:
                        if word not in wordlist:
                            wordlist.append(word)
                except Exception, e:
                    print e.message


        return wordlist

    def Construct_Matrix(self, sentence):
        Co_word_Matrix = np.zeros((len(self.wordlist),len(self.wordlist)))
        for i in range(len(sentence)):
            if i + self.time_window > len(sentence):
                window_word = sentence[i:]
            else:
                window_word = sentence[i: i + self.time_window]

            for word in window_word:
                row = self.wordlist.index(sentence[i])
                col = self.wordlist.index(word)
                Co_word_Matrix[row][col] = Co_word_Matrix[row][col] + 1

        return Co_word_Matrix
