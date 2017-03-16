

#http://nginx.org/en/download.html
import time
import urllib.request
from bs4 import BeautifulSoup

def downloadfile(URL,file_name):
    print(URL)
    urllib.request.urlretrieve(URL,filename=file_name)
    time.sleep(15)
    print("Downloaded")

def read_link(url):
    codeurl = url
    response = urllib.request.urlopen(codeurl)
    #print(response.read())
    soup = BeautifulSoup(response.read(),"lxml")

    links = soup.findAll("a",href=True)

    for link in links:
        file = link['href']
        if file.endswith(".zip"):
            filename= file.split("/")
            filename = filename[2]
            print(filename)
            url = "http://nginx.org" + file
            downloadfile(url,filename)

#http://nginx.org/download/nginx-0.7.69.zip
url = "http://nginx.org/en/download.html"
read_link(url)
