# -*- coding: utf-8 -*-
"""
Spyder Editor

author 03-180341 Takahiro Hori
"""
import codecs

class Weather():
    def __init__(self,file_name):#コンストラクタ
        fin = codecs.open(file_name,"r","shift_jis")
        fin.readline()
        self.__date,self.__hitmp,self.__lotmp,self.__rain,self.__sun = [],[],[],[],[]
        for line in fin:
            lst=line.strip().split(',')
            self.__date.append(lst[0])
            self.__hitmp.append(float(lst[1])) 
            self.__lotmp.append(float(lst[2]))
            self.__rain.append(float(lst[3]))
            self.__sun.append(float(lst[4]))
        fin.close()
    def __maxmin_t(self):#平均最大気温と平均最低気温
        print('平均最高気温は',"{:.4}".format(sum(self.__hitmp)/len(self.__hitmp)),'度です')
        print('平均最低気温は',"{:.4}".format(sum(self.__lotmp)/len(self.__lotmp)),'度です')
    def __max_rain(self):#最大の降水量と日時
        print('最大の降水は',self.__date[self.__rain.index(max(self.__rain))],'で',(max(self.__rain)),'mmです')
    def __ave_sun(self):#月ごとの平均日照時間
        month,sum_sun,date=0,0,0
        for i in range(len(self.__date)):
            dlst=self.__date[i].split('/')
            if(month==dlst[1]):
                sum_sun+=self.__sun[i]
                date+=1
            elif(month!=dlst[1]):
                if(month!=0):
                    print((self.__date[i-1].split('/'))[0],'年',(self.__date[i-1].split('/'))[1],'月の平均日照時間は',"{:.3}".format(sum_sun/date),'時間です')
                month=dlst[1]
                sum_sun=self.__sun[i]
                date=1
        print((self.__date[-1].split('/'))[0],'年',(self.__date[-1].split('/'))[1],'月の平均日照時間は',"{:.3}".format(sum_sun/date),'時間です')
    def summary(self):#private関数呼び出しのため
        self.__maxmin_t()
        self.__max_rain()
        self.__ave_sun()

       
tokyo_weather=Weather('tokyo-weather-20170601-20180531.csv')#クラス作成
tokyo_weather.summary()#関数の呼び出し