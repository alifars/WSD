# -*- coding: utf-8 -*-

import codecs
import nltk
from nltk.collocations import *


count=0
file=codecs.open('d:\\shirs.txt','r','utf-8')
colocfile=codecs.open('d:\\milkcol.txt','r','utf-8')
milkfile = codecs.open('d:\\wsd\\milk.txt','w','utf-8')
#lionfile = codecs.open('d:\\wsd\\lion.txt','w','utf-8')
#tapfile = codecs.open('d:\\wsd\\tap.txt','w','utf-8')
coloc=[]
for line in colocfile:
    print line
    coloc.append(line.strip())

for line in file:
    for item in coloc:
        if item in line:
            milkfile.write(line)
            milkfile.write('\n')
            print line

#    if line:
#       # print line
#       # tag=raw_input("lion,milk or another?")
#        if match1 in line or  match2 in line or match3 in line or match4 in line or match5 in line or match6 in line or match7 in line:
#            milkfile.write(line)
#            milkfile.write('\n')
#
#        elif match8 in line or match9 in line or match10 in line:
#            lionfile.write(line)
#            lionfile.write('\n')
#        elif match11 in line:
#           tapfile.write(line)
#           tapfile.write('\n')
#           print line
#        else:
#            otherfile.write(line)
#            otherfile.write('\n')

print count
file.close()
milkfile.close()
#lionfile.close()
#tapfile.close()
