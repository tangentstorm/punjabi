import os, re
import urllib as ul

path = "intro1.asp"
dirmap={'playsound':'mwords', 'playsound1':'alphabets'}

html = open(path).read()
for p, k in re.findall(r"(playsound1?)\('soundcell','(.*?)'\)", html):
    print "wget http://learnpunjabi.org/%s/%s.wav; sleep 0.25" % (dirmap[p], ul.quote(k))



