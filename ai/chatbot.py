# เขียนโดย นาย วรรณพงษ์  ภัททิยไพบูลย์
# https://python3.wannaphong.com/2014/11/ปัญญาประดิษฐ์ใน-python-ความฝั.html
while True:
    Input = input(">>> ")
    if Input in ['hi', 'HI', 'Hi']:
        print("Hello")
    elif Input in ['สวัสดี', 'ไง']:
        print("สวัสดี")
    else:
        print("เสียใจ เราไม่เข้าใจที่คุณกรอกมา")
