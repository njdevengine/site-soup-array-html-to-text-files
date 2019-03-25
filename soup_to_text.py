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
    
import os
path = os.getcwd()
os.mkdir(path+"/my_files")
    
########OUTPUT my_soup to text######
import codecs
for i in range(0,len(my_soup)-1):
    text_ = codecs.open("/my_files/hard_money_output_"+str(i+1)+".txt", "w", "utf-8")
    text_.write(my_soup[i])
    text_.close()
