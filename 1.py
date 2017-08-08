# coding: utf-8

import codecs
import re
import sys

fp=open("1.log","r")  
count=0;  
for s in fp.readlines():  
    li=re.findall("xxx", s)
    if len(li)>0:  
        count=count+len(li)
        print s
print("search:",count,">>>hello")  
fp.close()  
