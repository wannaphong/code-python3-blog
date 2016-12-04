# อ่านบทความ https://python3.wannaphong.com/2016/09/ซิงค์ข้อมูลด้วย-python.html
from dirsync import sync
import os
sourcedir=r"C:\11"
targetdir=os.getcwd() # รับที่ตั้งโฟลเดอร์ที่ไฟล์ python รันอยู่
sync(sourcedir, targetdir, "sync") # sync คือ ซิงค์ไฟล์
