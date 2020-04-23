from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import os
from lxml.html import fromstring
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
import re
driver = webdriver.Chrome(executable_path= r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver.close()

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
get_proxies()
proxies = get_proxies()
proxy_pool = cycle(proxies)
logger.debug("proxies: {}" .format(proxies))


book = input("enter the name of the book you want to download :")
logger.debug("book_name : {}" .format(book))
book_name = book.replace(" ","%20")
print(book_name)
URL = "https://b-ok.cc/s/" + book_name
#print(URL)
logger.debug("book url : {}" .format(URL))
#URL = 'https://b-ok.cc/s/how%20to%20blow%20her%20mind%20in%20bed'

for i in range(1,11):
    proxy = next(proxy_pool)
    r = requests.get(URL, proxies={"http": proxy, "https": proxy}) 
    r.encoding = 'ISO-8859-1'
    soup =  BeautifulSoup(r.text, 'html.parser')
    l = []
    pattern = "/book/\d+/"
    for link in soup.find_all('a'):
        string = link.get('href')
        match = re.search(pattern,str(string))
        if match:
            l.append(link.get('href'))
    try:
        url_2 = 'https://b-ok.cc/' + l[0]
        print(url_2)
        r_2 = requests.get(url_2 ,proxies={"http": proxy, "https": proxy})
        r_2.encoding = 'ISO-8859-1'
    except IndexError:
        print('no such book available')
    try:
        driver.get(url_2)
        driver.implicitly_wait(20)
        content = driver.find_element_by_class_name("btn-group")
        download = content.find_element_by_tag_name('a')
        print(download.text)
        download.click()
        driver.close()
    except :
        print('enough downloads for a day')