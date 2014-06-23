import codecs
import glob
import nt


file=codecs.open('d:\\wsd\\lion.txt','r','utf-8')

nt.chdir('d:\\wsd2\\lion')

counter=0
for line in file:
    # print name
     counter+=1
     filename='file'+str(counter)+'.txt'
     print filename

     file=codecs.open(filename,'w','utf-8')
     file.write(line)
     file.close()