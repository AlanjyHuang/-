class detector:
    def __init__(self,r,g,b):
        count =0
        array = []
        self.r=r
        self.g=g
        self.b=b
        
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
    mydetector=detector(255,255,0)
    print(mydetector.test())