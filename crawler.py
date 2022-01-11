from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os, json, time
from datetime import datetime
class Fetch:
    def __init__(self):
        
        self.sign=["白羊座","金牛座","雙子座","巨蟹座","獅子座","處女座","天秤座","天蠍座","射手座","摩羯座","水瓶座","雙魚座"]
        self.data = {}
        self.data["starsign"] = {}
        self.setBrowser()
        if not (os.path.exists("data.json")):
            self.get_allstarsign()
        self.start()
    def start(self):
        now=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        now=now.split('-')
        with open("data.json", "r") as f:
            data=json.load(f)
        f.close()
        before=data['updateTime'].split('-')
        if self.oneday(now,before):
            self.get_allstarsign()
    def setBrowser(self):
        with open("drivePath.txt", "r") as f:
            self.drivePath = f.read().strip()
        options = webdriver.ChromeOptions()
        options.add_argument("-headless")
        self.browser = webdriver.Chrome(executable_path=self.drivePath,
                                        options=options)
    def get_allstarsign(self):
        for i in self.sign:
            self.get_html(i)
            self.data["starsign"][i] = self.luckycolor[-1]
        self.writedata()
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
        if starsign=='白羊座':
            starsign='牡羊座'
        from urllib.request import urlopen
        url = "https://www.elle.com/tw/starsigns/today/"
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        All_starsigns = bsObj.findAll("a", {"class": "custom-item-title item-title"})
       # All_starsigns= self.browser.find_element_by_link_text(starsign)
        for i in All_starsigns:
            #print(i.get_text())
            #print(starsign)
            if i.get_text()==str(starsign):
                print(i['href'])
                url=urljoin(url,i['href'])
        self.get_color(url)
    def get_color(self,url):
        self.browser.get(url)
        print(url)
        bsObj = BeautifulSoup(self.browser.page_source, "html.parser")
        description = bsObj.find("ul",{"class":"body-ul"})
        description= description.findAll("li")
        description=list(description[2].get_text())
        color=''.join(description[5:])
        
        self.luckycolor=color
    
    def writedata(self):
        self.data["updateTime"] = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        with open("data.json", "w",encoding='Utf-8') as f:
            json.dump(self.data,f)
        f.close()

    def end(self):
        self.browser.close()
    def oneday(self,now,before):
        for i in range(0,3): 
            print(now[i],before[i])
            if(now[i]>before[i]):   
                return True
        
        return False
if __name__=='__main__':
    mysearch=Fetch()
    #if mysearch.isin("金牛座"):
        #mysearch.get_html("金牛座")
    #mysearch.get_starsign("金牛座")
    #print(mysearch.luckycolor)
    mysearch.end()