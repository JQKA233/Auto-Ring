from playsound import playsound
import time
import sys
 
def ring1():
    playsound('20.wav')#12
def ring2():
    playsound('10.wav')#8
def timeoff(hour,minute):
    if hour == time.localtime().tm_hour and minute == time.localtime().tm_min:
        ring1()
def timeon(hour,minute):
    if hour == time.localtime().tm_hour and minute == time.localtime().tm_min:
        ring2()
def timecheck():
    if time.localtime().tm_hour>=6 and time.localtime().tm_hour<=21:
        timeoff(7,0)#早自习开始
        timeoff(7,30)#第一节上课
        timeoff(8,20)#第二节上课
        timeoff(9,10)#第三节上课
        timeoff(10,00)#第四节上课
        timeoff(10,45)#第五节上课
        timeoff(13,0)#第六节上课
        timeoff(13,50)#第七节上课
        timeoff(15,0)#自习一
        timeoff(15,50)#自习二
        timeoff(16,40)#晚课一
        timeoff(18,50)#晚课二
        timeoff(20,30)#晚课三
        #timeon(7,28)#早自习下课
        timeon(8,10)#第一节下课
        timeon(9,0)#第二节下课
        timeon(9,50)#第三节下课
        timeon(10,40)#第四节下课
        timeon(11,25)#第五节下课
        #timeon(12,55)#起床号
        timeon(13,40)#第六节下课
        timeon(14,30)#第七节下课
        timeon(15,40)#自习间休一
        timeon(16,30)#自习间休二
        timeon(18,10)#干饭！
        timeon(20,20)#晚课间休
        timeon(21,50)#下班！
    else:
        sys.exit()
while 1:
    timecheck()
    time.sleep(60)#每60秒检查一次
    #pip3 install pyinstaller -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
    #python pyinstaller.py -F test_app.py