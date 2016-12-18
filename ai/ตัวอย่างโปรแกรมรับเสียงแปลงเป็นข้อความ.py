# เขียนโดย นาย วรรณพงษ์  ภัททิยไพบูลย์
# https://python3.wannaphong.com/2015/03/ประยุกต์โปรแกรมภาษา-python.html
__author__ = 'วรรณพงษ์'
import sys
#import โมดูลงาน GUI
from PySide.QtCore import *
from PySide.QtGui import *
####
from gtts import gTTS #โมดูลระบบสังเคราะห์เสียงพูด
import pyglet #โมดูลงานระบบเล่นไฟล์เสียง

import speech_recognition as sr #โมดูลรับเสียง
r = sr.Recognizer() 

def sayHello():
    #ระบบสังเคราะห์เสียงพูด
    def speak():
        tts = gTTS(text=say,lang='th') # text คือ ข้อความ lang คือ รหัสภาษา
        tts.save('hello-thai.mp3')
        #ระบบเล่นไฟล์เสียง
        music = pyglet.resource.media('hello-thai.mp3') #ดึงไฟล์เสียงเข้ามา
        music.play()
    #ระบบรับเสียง
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        say = r.recognize_google(audio,language = "th-TH") #กำหนดค่าภาษาเป็นภาษาไทย
        textEdit = QTextEdit(say) #เรียกใช้งาน QTextEdit มีลักษณะเป็น Textarea ครับ
        layout.addWidget(textEdit)
        #ส่วนปุ่มฟังข้อความ
        button2 = QPushButton("ฟังข้อความ") #กำหนดข้อความในปุ่ม
        button2.resize(75, 30) #กำหนดขนาดของปุ่ม
        button2.clicked.connect(speak) #เชื่อมต่อกับ sayHello
        layout.addWidget(button2)
        ###
    except LookupError:                            # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
        print("Could not understand audio")
#หน้าต่าง GUI
app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle("โปรแกรมรับเสียงแปลงเป็นข้อความแล้วสังเคราะห์เสียงข้อความ") #กำหนดชื่อตรงหัวโปรแกรม

layout = QVBoxLayout()
widget.setLayout(layout)

button = QPushButton("รับเสียง") #กำหนดข้อความในปุ่ม
button.resize(75, 30) #กำหนดขนาดของปุ่ม
button.clicked.connect(sayHello) #เชื่อมต่อกับ sayHello

layout.addWidget(button)
widget.show() #แสดงหน้าต่าง GUI
app.exec_()
