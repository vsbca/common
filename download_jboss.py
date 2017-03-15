#http://jbossas.jboss.org/downloads/
#!/usr/bin/env python3
import time
import urllib.request
from bs4 import BeautifulSoup

def downloadfile(URL,file_name):
    urllib.request.urlretrieve(URL,filename=file_name)
    time.sleep(10)
    print("Downloaded")


def read_link(url):
    codeurl = url
    response = urllib.request.urlopen(codeurl)
    #print(response.read())
    soup = BeautifulSoup(response.read(),"lxml")

    links = soup.findAll("a",href=True)

    for link in links:
        file = link['href']
        if "/files/" in file:
            if file.startswith("http://sourceforge.net") or file.startswith("http://jboss"):
                filename = file.split("/files/")
                filename=filename[1]
                filename=filename.replace("/","-")
                filename=filename+ ".zip"
                print(filename)
                downloadfile(file,filename)

url = "http://jbossas.jboss.org/downloads/"
read_link(url)
