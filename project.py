# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 20:16:56 2014

@author: Ankit Sharma
"""
import urllib2
from bs4 import BeautifulSoup
import re

words = []
with open('words.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        words = row

result = []
for word in words:
    definition = None
    mnemonic = None
    defn=1
    mnem=1
    url = 'http://mnemonicdictionary.com/?word=' + str(word)
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    divTag = soup.find_all("div",{"id":"home-middle-content"})

    for tag in divTag:
        dTags = tag.find("div")
        if dTags==None:
            defn=0
            continue
        definition = dTags.contents[3].strip()
        mTags = tag.find_all("div", {"class":"span9"})
        if len(mTags)<2:
            mnem=0
            continue        
        mnemonic = mTags[0].text.strip()

    if defn==0 or mnem==0:
        print "--------------- Not found"
        continue
    
    print "=============== Found"
    word_mnemonic = word + "$" + definition + "$" + mnemonic
    word_mnemonic_cleaned = re.sub(r'[^a-zA-Z0-9$]', ' ',word_mnemonic)
    result.append(word_mnemonic_cleaned)
    print result

#print result
myfile = open("result.csv","wb")
print >>myfile, '\n'.join(result)
