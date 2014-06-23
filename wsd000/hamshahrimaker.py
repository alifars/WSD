# -*- coding: utf-8 -*-
import codecs
from nltk.corpus.reader.xmldocs import XMLCorpusReader
from nltk.corpus.util import LazyCorpusLoader
import pyodbc

def correctPersianString(source):
    if source is not None:
        source = source.strip()#.replace("\\b\\s{2,}\\b", " ")

        #replace shift x with persian ye
        source = source.replace(u'\u064a', u'\u06cc' )

        #replace arabic k with persian k
        source = source.replace(u'\u0643', u'\u06a9' )

        #replace h dar shift+n
        source = source.replace(u'\u0623', u'\u0627' )

        #persian z
        source = source.strip().replace(u'\u0632\\s', u'\u0632' )

        #persian d
        source = source.strip().replace(u'\u062F\\s',u'\u062F' )

        #persian r
        source = source.strip().replace(u'\u0631\\s',   u'\u0631' )

        #persian zhe
        source = source.strip().replace(u'\u0698\\s',   u'\u0698' )

        #persian vav
        source = source.strip().replace(u'\u0648\\s',u'\u0648' )

        #persian dal zal
        source = source.strip().replace(u'\u0630\\s', u'\u0630' )

        #persian alef bi kolah
        source = source.strip().replace(u'\u0627\\s',       u'\u0627' )

        #persian alef ba kolah
        source = source.strip().replace(u'\u0622\\s',   u'\u0622' )

        return source


connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\farsnettest.mdb")
c = connection.cursor()
#c.execute("select number,example from shir")
corpus = LazyCorpusLoader('hamshahricorpus',XMLCorpusReader, r'(?!\.).*\.xml')
word=u'شیر'
targ = 0
c.execute("select * from shir")
for row in c:
    print row

#out = codecs.open('d:\\shirham.txt','w','utf-8')
for file in corpus.fileids():
#
#   #if num==1000: break
   for doc in  corpus.xml(file).getchildren():
#
          cat=doc.getchildren()[3].text#
          text=doc.getchildren()[5].text
          newtext=correctPersianString(text)
          allwords=text.split()
          sents=newtext.split('.')

          for sent in sents:


             if word in sent.split():
                 targ+=1
                # print targ
                 if sent:
                     c.execute("insert into shir(number, example) values ('pyodbc', 'awesome library')")




                # c.execute('insert into shir(number,example) values(?,?)',(targ,sent))


print targ

c.close()
#out.close()