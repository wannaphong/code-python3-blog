# เขียนโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
# https://python3.wannaphong.com/2016/07/ทำ-nlp-ในภาษา-python-postaggers-ภาษาไทย.html
from collections import Counter
text = ['แมว','ชอบ','ปลา','และ','แมว','ชอบ','นอน','มาก','เลย','คน','เลี้ยง','กลาย','เป็น','ทาส','แมว']
cnt = Counter(text) # นับจำนวนคำที่อยู่ใน list
print(cnt)
