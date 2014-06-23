# -*- coding: utf-8 -*-
import random

import codecs, glob, nt

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.classify import NaiveBayesClassifier
from nltk.classify import DecisionTreeClassifier
from nltk.classify.util import accuracy
import sys


def bag_of_words(words):
    return dict([(word, True) for word in words])


def get_feature(word):
    return dict([(word, True)])


def extract_words(text):
    match=u'شیر'
    stopwords = [u'تا', u'که', u'از', u'و', u'با', u'مي', u'شود', u'است', u'يا', u'اما',
                 u'اين', u'آن', u'دارد', u'شوند', u'کنند', u'آنها', u'هاي'
                                                                    u'براي', u'بوده', u'بود', u'بايد', u'می‌شوند',
                 u'می‌کنند', u'می‌شود', u'نيز', u'می‌باشد', u'هستند',
                 u'بوده', u'دارند', u'هست', u'اگر', u'می‌دهد ', u'اينها',
                 u'می‌شوند', u'شدند', u'می‌باشند', u'دهند', u'می‌دهند', u'همچنان', u'كند', u'ها', u'می']

    newwords = []
    for word in stopwords:
        word = word.replace(u'\u064a', u'\u06cc')
        word = word.replace(u'\u0643', u'\u06a9')
        newwords.append(word)

    tokens = text.split()
    nudetokens = []
    for token in tokens:
        token = token.strip(u'.,،)(:')

        nudetokens.append(token)

    result = [x for x in nudetokens if x not in newwords and len(x) > 2 and x!=match]
    #    for i in  result:
    #        print i
    return result


##file=codecs.open('d:\lion.txt','r','utf-8')
##file2=codecs.open('d:\milk.txt','r','utf-8')
filenames = glob.glob('d:\\wsd\\*.txt')
nt.chdir('d:\\wsd')
feat_set = []
sets = []
for name in filenames:
# print name

    filename = name.split('\\')[-1]
    sense = name.split('\\')[-1].split('.')[0]
    print 'training', sense
    file = codecs.open(filename, 'r', 'utf-8')
    text = file.read()
    features = extract_words(text)
    #
    #     for item in sorted(features):
    #          print item


    feat_set = feat_set + [(get_feature(word), sense) for word in features]
random.shuffle(feat_set)
random.shuffle(feat_set)
for item in feat_set:
    print item
def train_feats(feat_set):
    train_feats = []
    trainlen = int(.25 * len(feat_set))
    for item in feat_set[trainlen:]:
        train_feats.append(item)

    #        print i
    return train_feats


def test_feats(feat_set):
    test_feats = []
    trainlen = int(0.4 * len(feat_set))
    # print trainlen
    for item in feat_set[:trainlen]:
        test_feats.append(item)

 
    return test_feats

#milkfile=codecs.open('d:\\wsd\\milk.txt','a','utf-8')
#tapfile=codecs.open('d:\\wsd\\tap.txt','a','utf-8')
train = train_feats(feat_set)
test = test_feats(feat_set)
classifier = NaiveBayesClassifier.train(train)
#classifier = DecisionTreeClassifier.train(train)
print accuracy(classifier, test) * 100

match = u'شیر'
file = codecs.open('d:\\wsd\\otherfile.txt', 'r', 'utf-8')
for line in file:
    if match in line.split():
        tokens = bag_of_words(extract_words(line))
        decision = classifier.prob_classify(tokens)
       # decision = classifier.classify(tokens)
        print line,decision
        #       if decision.max()=='tap':
        #           print line
#        result = "%s - %s" % (decision, line )
#        #if decision=='lion':
#        #         milkfile.write(line)
#        #         milkfile.write('\n')
#        if decision.prob('milk') > .9:
#            print line

file.close()