# -*- coding: utf-8 -*-

import codecs
import nltk
from nltk.collocations import *
from pattern.web import Google, SEARCH, plaintext, Wikipedia, Newsfeed, Yahoo, Bing, Twitter

#count=0
#milkfile=codecs.open('d:\\webmilk.txt','w','utf-8')
#lionfile=codecs.open('d:\\weblion.txt','w','utf-8')
#tapfile = codecs.open('d:\\webtap.txt','w','utf-8')
#
#engine = Google(license=None)
#
#
#match=u'شیر جنگل'
#for i in range(1,200):
#   for result in engine.search(match, type=SEARCH, start=i):
#        print result.description
#       # print result.url