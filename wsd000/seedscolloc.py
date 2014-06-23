# -*- coding: utf-8 -*-
import codecs
import nltk
from nltk.collocations import *

stoplist=[u'و',u'به',u'از',u'در',u'بر',u'را',u'با',u'که',u'های',u'می',u'یا',u'برای',
           u'است',u'تا',u'آن',u'دارد',u'شود',u'او',u'ها',u'هم',u'شده',u'کند',u'من',u'ای',u'هر',
           u'کنند',u'کند','دهند','اگر',u'آنها',u'دهند',u'اش', u'شد', u'اگر',u'.',u'،',u'این',u'اینها',
           u'بود',u'کرد',u'کردند',u'وی', u'باشد',u'باشند',u'خود',u'بود',u'شد',
           u'زیرا',u'اما',u'ولی',u'چون',u'اند',
           u'دارند',u'شوند',u'می',u'هایش',u'هایشان',u'هایت',u'هایم',u'یک',u'گفت',
           u'نیز',u'مانند',u'هایی',u'کرده',u'کردن',u'بی',u'دهد',
           u'نمی',u'ام',u'هایتان',u'نه',u'آیا',u'دیگر',u'هستند',u'بودند',u'نیست',u'نیستند',u'درباره',
           u'کنید',u'همه',u'هیچ',u'خواهد',u'همین',u'چه',u'چرا',u'کنیم',u'داد',
           u'توان',u'تواند',u'شما',u'حتی',u'مثل']
match=u'شیر'
count=0
outfile=codecs.open('d:\\shirs.txt','r','utf-8')
tapcolocfile=codecs.open('d:\\tapcol.txt','w','utf-8')
lioncolocfile=codecs.open('d:\\lioncol.txt','w','utf-8')
milkcolocfile=codecs.open('d:\\milkcol.txt','w','utf-8')
#

text = outfile.read()
tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
#finder = TrigramCollocationFinder.from_words(tokens)
finder.apply_word_filter(lambda w: w  in stoplist)


bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

#scored = finder.score_ngrams(bigram_measures.raw_freq)
scored= finder.nbest(bigram_measures.raw_freq , 1000)
c=0
for item in  scored:
  #  print item[0],item[1]

    if match in item:

      print item[0],item[1]
      tag=raw_input('L,M,T,N   :')

      if tag == 'l':

          lioncolocfile.write(item[0]+' '+item[1])
          lioncolocfile.write('\n')
      elif  tag == 'm':
          milkcolocfile.write(item[0]+' '+item[1])
          milkcolocfile.write('\n')
      elif  tag == 't':
          tapcolocfile.write(item[0]+' '+item[1])
          tapcolocfile.write('\n')
      elif tag=='n':
          pass

tapcolocfile.close()
lioncolocfile.close()
milkcolocfile.close()