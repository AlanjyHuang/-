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
| LED顯示板     | 1    | 蝦皮($30)       |
| webcam        | 1    | 蝦皮($699) |
| 杜邦線        | 數條 | 親友友情贊助  |
| 水管          | 數條 | 親友友情贊助   |

## Technique
<img src="https://user-images.githubusercontent.com/67900973/149155179-1f9a3e8b-53a3-4c87-8809-dbee33114aea.jpeg" width="300px"/>
<img src="https://user-images.githubusercontent.com/67900973/149158853-be2670db-5bb1-4805-884a-cd5cf8bc9332.jpeg" width="300px"/>
<img src="https://user-images.githubusercontent.com/67900973/149158993-54349034-194c-460f-9191-d17d92f9d018.jpeg" width="300px"/>
## Implementation Process

## Installation

#### 噴水


#### LED

#### Webcam
- 先更新軟體套件
    ```terminal=
    sudo apt update
    sudo apt upgrade
    ```

- 確認webcam裝置
    ```terminal=
    sudo lsusb
    ```

    <img width="502" alt="image" src="https://user-images.githubusercontent.com/81890797/149152823-eb558ad1-4b11-430e-a3ad-ad23930b4d60.png">

- 安裝numpy套件
    ```terminal=
    pip install numpy
    ```

- 安裝opencv
    ```terminal=
    sudo apt-get install libopencv-dev
    ```

- 程式碼 - ReadWebcam.py
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

- 程式碼 - detectcolor.py
    根據rgb分析其對應到的顏色

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

## Job Assignment

### 林佑諺

- 硬體設備 + 控制程式

### 潘世瑋

- 硬體設備 + 控制程式

### 廖志遠

- webcam + 影像辨識

### 黃舟淵

- telegram bot
- 網路爬蟲

## Reference

-   https://ithelp.ithome.com.tw/users/20130283/ironman/3553
-   https://blog.csdn.net/jcdjx/article/details/38457271
