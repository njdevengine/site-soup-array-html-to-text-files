#save your sites here
sites = ["https://www.site1.com"]

#scrapes the sites and dumps html into my_soup array (decoded from bytes)
from urllib.request import Request, urlopen
length = len(sites)-1
my_soup = []
for i in range(0,length):
    try:
        req = Request(sites[i], headers={"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
        webpage = urlopen(req).read()
        print(webpage)
        my_soup.append(webpage.decode("utf-8"))
    except Exception as e: print(e)
        
######CREATE SOME DIRECTORIES######
import os
path = os.getcwd()
os.mkdir(path+"/my_files")
os.mkdir(path+"/analysis")
    
######OUTPUT my_soup to text######
import codecs
for i in range(0,len(my_soup)-1):
    text_ = codecs.open("/my_files/output_"+str(i+1)+".txt", "w", "utf-8")
    text_.write(my_soup[i])
    text_.close()

######COMBINE TEXT FILES######
import shutil
import glob

with open("combined.txt", 'wb') as outfile:
    for filename in glob.glob('my_files/*.txt'):
        if filename == outfile:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)

######HTML CLEANUP######

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import re

with open('combined.txt', 'r', encoding="utf-8") as myfile:
    string = myfile.read().replace('\n', ' ')
    string = string.lower()
    
regex = re.compile('[^a-zA-Z]')
string = regex.sub(' ', string)

words = string.split(" ")

for word in words:
    word.lower()

words = list(filter(None, words))
dfphrase1 = pd.DataFrame({"words" : words})
grouped1 = dfphrase1["words"].value_counts()
grouped1 = grouped1.to_frame()
grouped1.rename(columns={"words":"count"})

phrase = []
num = len(words)-1
for n in range(0,num):
        phrase.append(words[n]+" "+words[n+1])
dfphrase2 = pd.DataFrame({"phrase" : phrase})
grouped2 = dfphrase2["phrase"].value_counts()
grouped2 = grouped2.to_frame()
grouped2.rename(columns={"phrase":"count"})

phrase3 = []
num = len(words)-2
for n in range(0,num):
        phrase3.append(words[n]+" "+words[n+1]+" "+words[n+2])
        
dfphrase3 = pd.DataFrame({"phrase3" : phrase3})
grouped3 = dfphrase3["phrase3"].value_counts()
grouped3 = grouped3.to_frame()
grouped3.rename(columns={"phrase3":"count"})

#dfphrase1.head()
#dfphrase2.head()
#dfphrase3.head()

#grouped1.head()
#grouped2.head()
#grouped3.head()

writer = pd.ExcelWriter('analysis/analysis_output.xlsx', engine = 'xlsxwriter')
grouped1.to_excel(writer, sheet_name='grouped1')
grouped2.to_excel(writer, sheet_name='grouped2')
grouped3.to_excel(writer, sheet_name='grouped3')
writer.save()
