from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os, json, time

class Fetch:
    def __init__(self):
        self.sign=["白羊座","金牛座","雙子座","巨蟹座","獅子座","處女座","天秤座","天蠍座","射手座","摩羯座","水瓶座","雙魚座"]
    def setBrowser(self):
        with open("drivePath.txt", "r") as f:
            self.drivePath = f.read()[:-1]
        options = webdriver.ChromeOptions()
        options.add_argument("-headless")
        self.browser = webdriver.Chrome(executable_path=self.drivePath,
                                        options=options)
    def isin(self,star):
        if star in self.sign:
            return True
        else:
            return False
    def get_starsign(self,starsign):
     
        url = "https://www.elle.com/tw/starsigns/today/"
        self.browser.get(url)
  
        bsObj = BeautifulSoup(self.browser.page_source, "html.parser")
        All_starsigns = bsObj.findAll("a", {"class": "custom-item-title item-title"})
       # All_starsigns= self.browser.find_element_by_link_text(starsign)
        for i in All_starsigns:
            #print(i.get_text())
            if i.get_text()==starsign:
                print(i['href'])
                url=urljoin(url,i['href'])
        
        self.get_color(url)
    def get_html(self,starsign):
        from urllib.request import urlopen
        url = "https://www.elle.com/tw/starsigns/today/"
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        All_starsigns = bsObj.findAll("a", {"class": "custom-item-title item-title"})
       # All_starsigns= self.browser.find_element_by_link_text(starsign)
        for i in All_starsigns:
            #print(i.get_text())
            if i.get_text()==starsign:
                print(i['href'])
                url=urljoin(url,i['href'])
        self.get_color(url)
    def get_color(self,url):
        self.setBrowser()
        from bs4 import BeautifulSoup
        self.browser.get(url)
        print(url)
        bsObj = BeautifulSoup(self.browser.page_source, "html.parser")
        description = bsObj.find("ul",{"class":"body-ul"})
        description= description.findAll("li")
        description=list(description[2].get_text())
        color=''.join(description[5:])
        
        self.luckycolor=color
        
    def end(self):
        self.browser.close()

if __name__=='__main__':
    mysearch=Fetch()
    if mysearch.isin("金牛座"):
        mysearch.get_html("金牛座")
    #mysearch.get_starsign("金牛座")
    print(mysearch.luckycolor)
    mysearch.end()