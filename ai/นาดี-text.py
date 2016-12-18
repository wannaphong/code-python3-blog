# Bot นาดี AI ผู้ช่วยต้นแบบ
# make1
#License: BSD
# เขียนโดย นาย วรรณพงษ์  ภัททิยไพบูลย์
# https://python3.wannaphong.com/2015/03/สั่งงานด้วยเสียงใน-python.html
__author__ = 'วรรณพงษ์'
#License: BSD
import PyICU #ใช้ในการตัดคำ
import re
import webbrowser #ใช้ในการค้นหาโดยเปิด web browser แล้วค้นผ่านกูเกิล
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
######################
print("สวัสดีค่ะ ฉันชื่อ นาดี ยินดีที่ได้รับใช้ค่ะ :)")
while True:
    a = input("Text : ") #รับข้อความ
    txt = [warp(a)] #ตัดคำจากตัวแปร a
    txt = (','.join(str(x) for x in txt))
    if txt.find("สวัสดี") == 0 or txt.find("ไง") == 0 or txt.find("หวัดดี") == 0: #ถ้าค้นแล้วเจอคำเหล่านี้
        print("สวัสดีค่ะ ฉันชื่อ นาดี ค่ะ")
    elif txt.find("ออก") == 0 & txt.find("ระบบ") == 0: #ถ้าค้นแล้วเจอคำเหล่านี้
        print("ลาก่อน :(")
        break #ออกจากการลูปวน
    elif txt.find("ค้นหา") == 0 & txt.find("ว่า") == 0: #ถ้าค้นแล้วเจอคำเหล่านี้
        s = txt.split("ว่า") #แบ่งคำตรงคำว่า "ว่า"
        a = str(s[1])
        a = a.replace(',', '') #เอา , ออก
        webbrowser.get('windows-default').open_new_tab('https://www.google.co.th/search?q=%s' % a) #ค้นหา
    elif txt.find("เวลา") == 0 & txt.find("เท่า") == 0 or txt.find("ตอน") == 0 & txt.find("นี้") == 0: #ถ้าค้นแล้วเจอคำเหล่านี้
        a = time.strftime("%H - %M :") #บอกเวลาแบบ 24 ชั่วโมง
        a = a.replace('-', 'นาฬิกา') #แทนที่
        a = a.replace(':', 'นาที') #แทนที่
        print("ขณะนี้เป็นเวลา %s ค่ะ" % a) #แสดงผลลัพธ์
    else:
        print("ขออภัยค่ะ\nระบบไม่รู้จักคำสั่งนี้")
