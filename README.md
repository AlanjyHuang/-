# -

## Concept Development

**答案是紫色，因為外星人不戴帽子，所以綠色好討厭**

## Ingredients

| 名稱          | 數量 | 來源            |
| ------------- | ---- | --------------- |
| raspberry pi3 | 1    | MOLi            |
| 繼電器        | 1    | 電子材料行($60) |
| 抽水馬達(5V)  | 2    | 蝦皮($26)       |
| 麵包版        | 1    | 電子材料行($30) |
| LED 顯示板    | 1    | 蝦皮($30)       |
| webcam        | 1    | 蝦皮($699)      |
| 杜邦線        | 數條 | 親友友情贊助    |
| 水管          | 數條 | 親友友情贊助    |

## Technique

<img src="https://user-images.githubusercontent.com/67900973/149155179-1f9a3e8b-53a3-4c87-8809-dbee33114aea.jpeg" width="300px"/>
<img src="https://user-images.githubusercontent.com/67900973/149158853-be2670db-5bb1-4805-884a-cd5cf8bc9332.jpeg" width="300px"/>
<img src="https://user-images.githubusercontent.com/67900973/149158993-54349034-194c-460f-9191-d17d92f9d018.jpeg" width="300px"/>
<img src="https://user-images.githubusercontent.com/67900973/149160147-f09d1797-82b2-4de2-95f7-8cadff48c07e.jpeg" width="300px"/>
<img src="https://user-images.githubusercontent.com/67900973/149160155-a2e94984-58e8-40b4-a92f-e1c4dc677a78.jpeg" width="300px"/>

## Installation

#### 噴水

#### LED

#### Webcam

-   先更新軟體套件

    ```terminal=
    sudo apt update
    sudo apt upgrade
    ```

-   確認 webcam 裝置

    ```terminal=
    sudo lsusb
    ```

      <img width="502" alt="image" src="https://user-images.githubusercontent.com/81890797/149152823-eb558ad1-4b11-430e-a3ad-ad23930b4d60.png">

-   安裝 numpy 套件

    ```terminal=
    pip install numpy
    ```

-   安裝 opencv

    ```terminal=
    sudo apt-get install libopencv-dev
    ```

-   程式碼 - ReadWebcam.py
    感測 rgb 數值

    ```terminal=
    # importing required libraries
    import cv2
    import numpy as np
    import time
    class color:
        def run(self):
    # taking the input from webcam
            vid = cv2.VideoCapture(0)

            timers = 5

    # running while loop just to make sure that
    # our program keep running untill we stop it
            while timers>0:

                # capturing the current frame
                _, frame = vid.read()

                # displaying the current frame
                #cv2.imshow("frame", frame)

                # setting values for base colors
                b = frame[:, :, :1]
                g = frame[:, :, 1:2]
                r = frame[:, :, 2:]

                # computing the mean
                b_mean = np.mean(b)
                g_mean = np.mean(g)
                r_mean = np.mean(r)



                print("r:" + str(r_mean) + ",g:" + str(g_mean) + ",b:" + str(b_mean))

                    # displaying the most prominent color
                if (b_mean > g_mean and b_mean > r_mean):
                    print("Blue")
                if (g_mean > r_mean and g_mean > b_mean):
                    print("Green")
                else:
                    print("Red")

                time.sleep(1)
                timers -= 1
                return list([r_mean,g_mean,b_mean])
    ```

-   程式碼 - detectcolor.py
    根據 rgb 分析其對應到的顏色

    ```terminal=
    class detector:
    def __init__(self,r,g,b):
        count =0
        array = []
        self.r=int(r)
        self.g=int(g)
        self.b=int(b)

    def test(self):
        mx = max(self.r,self.g,self.b)
        mn = min(self.r,self.g,self.b)
        df = mx - mn
        if mx == mn:
            h = 0
        elif mx == self.r:
            h = (60 * ((self.g-self.b)/df)+ 360) % 360
        elif mx ==self.g:
            h = (60 * ((self.b-self.r)/df)+ 120) % 360
        elif mx ==self.b:
            h = (60 * ((self.r-self.g)/df)+ 240) % 360
        if mx == 0:
            s =0
        else:
            s = df/mx

        v = mx

        if v >= 0.5 and v<=0:
            return "黑"

        else:
            if s<=0.43:
                if v > 0.5:
                    return "白"
                else:
                    return "灰"
            else:
                if h>0 and h<30 or h>=330 and h<=360:
                    return "紅"
                elif h>=30 and h<90:
                    return "黃"
                elif h>=90 and h<210:
                    return "綠"
                elif h>=210 and h < 270:
                    return "藍"
                elif h>=270 and h< 330:
                    return "紫"

    if __name__=='__main__':
        r=input("R :")
        g=input("G :")
        b=input("B :")
        mydetector=detector(r,g,b)
        print(mydetector.test())
    ```

#### Telegram bot

    ```terminal=
    pip install -r requirements.txt
    ```
    - 創建telegrambot
        1.找到BotFather 輸入 /newbot
        ![圖片](https://user-images.githubusercontent.com/52521773/149160866-efdfcc8a-17b0-4a24-a7e9-c65035ecd08f.png)
        2.填完所資料(注意:username要使用OObot結尾)
        3.拿出token 並放入新建的檔案 LSA1101_bot_api.txt
        ![圖片](https://user-images.githubusercontent.com/52521773/149161632-216f9da3-c7b5-47f0-8f75-bbb41dd8b029.png)
        4.輸入/mybot 並選擇剛剛設定的telbot
        ![圖片](https://user-images.githubusercontent.com/52521773/149162024-9004c881-ebce-417f-97a0-0070989a9bb4.png)
        5.在Edite bot 中的 Edite command 輸入botcommand檔案中的命令，以此宣告命令
    - telegram_bot.py
        1.引入telegrambot python套件
        ```
            from telegram.ext import Updater # 更新者
            from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
            from telegram.ext import MessageHandler, Filters # Filters過濾訊息
            from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
        ```
        2.初始化bot
        ```
        self.updater = Updater(token=self.token, use_context=False) #放入token
        self.dispatcher = self.updater.dispatcher  #用來抓使用者丟給bot的命令
        self.dispatcher.add_handler(CommandHandler('/命令名稱', 命令的function))
        ```
        3.讓telegrambot 運作
        ```
        mybot.updater.start_polling()  #updater.start_polling()會讓他一直持續處理你定義的handeler直到關閉
        ```
    - crawler.py
        1.sudo apt-get install chromium-chromedriver #安裝chromedriver
        2.將安裝好的路徑放入drivePath.txt(請自己新建)
        3.設定driver
        ```
        with open("drivePath.txt", "r") as f:
            self.drivePath = f.read().strip()
        options = webdriver.ChromeOptions()
        options.add_argument("-headless")  #沒有圖形介面的裝置一定要加這個
        self.browser = webdriver.Chrome(executable_path=self.drivePath,
                                        options=options)
        ```
        4.抓取資料
        ```
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
        ```
        5.因為每次啟動都抓一次過於耗時，因此引入將抓到的資訊匯出並以nodejs儲存
        ```
        def start(self):
            now=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")  #判別距離上次抓取資料是否過去一天
            now=now.split('-')
            with open("data.json", "r") as f:
                data=json.load(f)
            f.close()
            before=data['updateTime'].split('-')
            if self.oneday(now,before):
                self.get_allstarsign()

        def writedata(self):  #寫入資料至檔案
            self.data["updateTime"] = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            with open("data.json", "w",encoding='Utf-8') as f:
                json.dump(self.data,f)
            f.close()
        ```
    - 主要telegrambo指令介紹:
        +off - 關機
            ```
            #呼叫updater.stop()停止telegrambot
            self.updater.stop()
            ```
        +luckycolor - 查詢星座幸運色
        依照使用者輸入的星座查詢幸運色，若使用者衣服與幸運色相同則恭喜，若不同則噴水逞罰，
        最後會用LED顯示查詢到的幸運色同時傳送給使用者
        ```
        def luckycolor(self,bot,update):
            message=update.message
            starsign=list(message['text'])
            starsign=starsign[12:]
            starsign=''.join(starsign)
            print(starsign)
            if starsign=="":
                update.message.reply_text(text='請在指令後方加入星座')
                return
            mysearch=crawler.Fetch()  #呼叫crawler.py 去抓你輸入的星座
            if mysearch.isin(starsign):
                update.message.reply_text(text='稍等一下，正在查詢....')
                with open("data.json", "r") as f:
                    data=json.load(f)
                f.close()
                update.message.reply_text(text='今天'+starsign+'的幸運顏色是: '+str(data['starsign'][starsign]))
                mysearch.end()
            else:
                update.message.reply_text(text='沒有'+starsign+'這個星座')
            #self.yourluckyday(str(data['starsign'][starsign]))
            searchcolor=str(data['starsign'][starsign])
            #detectcolor.detector()
            mycam=ReadWebcam.color()
            out=mycam.run()                                 #用webcam抓看到的顏色返還RGB
            mydetector=detectcolor.detector(out[0],out[1],out[2])  #輸入RGB返還一個顏色(中文字)
            color=mydetector.test()
            if(color==searchcolor):
                update.message.reply_text(text="你今天很幸運喔")
            else:
                update.message.reply_text(text="今天不是你的幸運日喔")
                mymotor=motor.motor()
                mymotor.blink(self.water)            #噴self.water的水量
            myled=LED.LED()                      #將RGB傳給 LED
            myled.start(5,out[0],out[1],out[2])
        ```
        +spray - 立即噴水
        ```
        mymotor=motor.motor()
        mymotor.blink(self.water)
        ```
        +set_waterpw - 設定self.water
        +hi -跟使用者打招呼
        從updater 抓使用者的姓名跟他打招呼
        ```
        message = update.message
        chat = message['chat']
        update.message.reply_text(text='HI  ' + str(chat['first_name'])+' '+str(chat['last_name']))
        ```
        +whatcolor - 觀察顏色回傳RGD
        呼叫Readwebcam 回傳看到的顏色

## Job Assignment

### 林佑諺

-   硬體設備 + 控制程式

### 潘世瑋

-   硬體設備 + 控制程式

### 廖志遠

-   webcam + 影像辨識

### 黃舟淵

-   telegram bot
-   網路爬蟲

## Reference

-   https://ithelp.ithome.com.tw/users/20130283/ironman/3553
-   https://blog.csdn.net/jcdjx/article/details/38457271
