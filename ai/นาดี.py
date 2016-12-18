# Bot นาดี AI ผู้ช่วยต้นแบบ
# make2
#License: BSD
# เขียนโดย นาย วรรณพงษ์  ภัททิยไพบูลย์
# https://python3.wannaphong.com/2015/03/สั่งงานด้วยเสียงใน-python.html
__author__ = 'วรรณพงษ์'
#License: BSD
import PyICU #ใช้ในการตัดคำ
import re
import webbrowser #ใช้ในการค้นหาโดยเปิด web browser แล้วค้นผ่านกูเกิล
from gtts import gTTS #โมดูลระบบสังเคราะห์เสียงพูด
import pyglet #โมดูลงานระบบเล่นไฟล์เสียง
import speech_recognition as sr #โมดูลรับเสียง
import time #ดึงเวลา
#ระบบตัดคำไทย
def isThai(chr):
    cVal = ord(chr)
    if(cVal >= 3584 and cVal <= 3711):
        return True
    return False
def warp(txt):
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    retTxt = ""
    try:
        while(1):
            currentPos = next(bd)
            retTxt += txt[lastPos:currentPos]
            #เฉพาะภาษาไทยเท่านั้น
            if(isThai(txt[currentPos-1])):
                if(currentPos < len(txt)):
                    if(isThai(txt[currentPos])):
                        #คั่นคำที่แบ่ง
                        retTxt += ','
            lastPos = currentPos
    except StopIteration:
        pass
        #retTxt = retTxt[:-1]
    return retTxt
#ระบบพูดและรับเสียง
class speak:
    def __init__(self,onetxt):
        self.onetxt = onetxt
        tts = gTTS(text=onetxt,lang='th') # text คือ ข้อความ lang คือ รหัสภาษา
        tts.save('hello-thai.mp3')
        #ระบบเล่นไฟล์เสียง
        music = pyglet.resource.media('hello-thai.mp3') #ดึงไฟล์เสียงเข้ามา
        music.play()
        def exit_callback(dt):
            return
        pyglet.clock.schedule_once(exit_callback,music.duration) #เช็คการทำงานระบบเล่นเสียง ไม่ให้เล่นซ้ำกัน
class text:
    def __init__(self,txtto):
            self.txtto = txtto
            #print(txtto)
            speak(txtto)
hello = text("สวัสดีค่ะ ฉันชื่อ นาดี ยินดีที่ได้รับใช้ค่ะ") #เสียงต้อนรับ
while True:
    r = sr.Recognizer() 
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        say = r.recognize_google(audio,language = "th-TH") #กำหนดค่าภาษาเป็นภาษาไทย
    except LookupError:
        say = "ไม่สามารถรับเสียงได้ค่ะ"
    txtcom = [warp(say)] #ตัดคำจากข้อความที่แปลงมาจากเสียง
    #ส่วนคำสั่ง
    txt = (','.join(str(x) for x in txtcom))
    if txt.find("สวัสดี") == 0 or txt.find("ไง")==0 or txt.find("หวัดดี") == 0:
        text("สวัสดีค่ะ ฉันชื่อ นาดี ค่ะ")
    elif txt.find("ออก") == 0 & txt.find("ระบบ") == 0:
        break
    elif txt.find("ค้นหา") == 0 & txt.find("ว่า") == 0: #ถ้าค้นแล้วเจอคำเหล่านี้
        s = txt.split("ว่า")
        s = str(s)
        a = s[1]
        a = a.replace(',', '')
        text("ค้นหาคำว่า %s" % a)
        webbrowser.get('windows-default').open_new_tab('https://www.google.co.th/search?q=%s' % a)
    elif txt.find("เวลา") == 0 & txt.find("เท่า") == 0 or txt.find("ตอน") == 0 & txt.find("นี้") == 0:
        a = time.strftime("%H - %M:")
        a = a.replace('-', 'นาฬิกา')
        a = a.replace(':', 'นาที')
        text("ขณะนี้เป็นเวลา %sค่ะ" % a)
    elif txt.find("พิมพ์") == 0 & txt.find("ตาม") == 0:
        import pyperclip
        text("กรุณาพูดออกมาค่ะ")
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            say = r.recognize(audio)
        except LookupError:
            say = "ไม่สามารถรับเสียงได้ค่ะ"
        txtcom = [warp(say)]
        txt = (','.join(str(x) for x in txtcom))
        pyperclip.copy(txt)
        text("ระบบได้คัดลอกที่พูดออกมาแล้ว")
    else:
        text("ขออภัยค่ะ ระบบไม่รู้จักคำสั่งนี้ค่ะ")
