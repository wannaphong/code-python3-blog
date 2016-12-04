# อ่านบทความได้ที่  https://python3.wannaphong.com/2016/12/ดึงข้อมูล-whois-โดเมนด้วย-python.html
# เขียนโดย วรรณพงษ์  ภัททิยไพบูลย์
import whois
w = whois.whois('abc.xyz') # กรอกโดเมนที่ต้องการข้อมูล Whois
print(w.expiration_date) # วั้นหมดอายุ
print(w.text) # รายละเอียดโดเมน
