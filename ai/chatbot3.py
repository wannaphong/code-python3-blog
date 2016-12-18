# ทำ Chat Bot ง่าย ๆ ในภาษา Python
# เขียนโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
#  https://python3.wannaphong.com/2015/07/ทำ-chat-bot-ง่าย-ๆ-ในภาษา-python.html
from tinydb import TinyDB, where # เรียกใช้งานโมดูล tinydb
import random
db = TinyDB('db.json') # เรียกใช้ฐานข้อมูลจากไฟล์ db.json
def addword():
	print("ไม่พบประโยคนี้ในระบบ คุณต้องการสอนไหม")
	addif = str(input("Y or N : "))
	if addif  == "Y":
		q = input("คำถาม : ")
		ans = input("คำตอบ : ")
		db.insert({q:ans}) # เพิ่มข้อมูลลงฐานข้อมูล
	else:
		print("Ok")

while True:
	text = input("> ")
	a = db.search(where(text)) # ค้นหาคำที่เหมือนกันในฐานข้อมูล
	if a == []:
		addword()
	else:
		a =  random.choice([a for a in db.search(where(text))]) # ทำการลูปในกรณีที่มีคำตอบมากและแยกกันกรอกข้อมูล แล้วทำการสุ่ม
		print(a[text])
