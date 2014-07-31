# -*- coding: utf-8 -*-
"""
@author: Ankit Sharma
@blog: diggdata.in

Created on Sat Jul 12 20:16:56 2014

"""
import urllib2
from bs4 import BeautifulSoup
import csv
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
    definition_found=1
    mnemonic_found=1
    url = 'http://mnemonicdictionary.com/?word=' + str(word)
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    divTag = soup.find_all("div",{"id":"home-middle-content"})

    for tag in divTag:
        dTags = tag.find("div")
        if dTags==None:
            definition_found=0
            continue
        definition = dTags.contents[3].strip()
        mTags = tag.find_all("div", {"class":"span9"})
        if len(mTags)<2:
            mnemonic_found=0
            continue        
        mnemonic = mTags[0].text.strip()

    if definition_found==0 or mnemonic_found==0:
        print "--------------- Word not found ---------------"
        continue
    
    word_mnemonic = word + "$" + definition + "$" + mnemonic
    word_mnemonic_cleaned = re.sub(r'[^a-zA-Z0-9$]', ' ',word_mnemonic)
    result.append(word_mnemonic_cleaned)
    print result

#print results to a file
myfile = open("result_test.csv","wb")
print >>myfile, '\n'.join(result)
