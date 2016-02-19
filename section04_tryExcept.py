# -*- coding: utf-8 -*-
# print 10/0

try:
    print "始まります。"
    print 10/0
    print "終わった?"
except Exception as e:
    print "エラー発生 : {0}".format(e)
finally:
    print "とにかくこれで終わりだ。"


try:
    print "Hello"
except:
    print "Bye"