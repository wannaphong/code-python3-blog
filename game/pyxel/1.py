import pyxel

pyxel.init(160, 120) # (ขนาดความกว้าง,ขนาดความยาวในหน่วยพิกเซล)

def update(): # ใช้สำหรับเวลามีการอัพเดต
    if pyxel.btnp(pyxel.KEY_Q): # ถ้ากดปุ่ม Q
        pyxel.quit() # ออก

def draw(): # ฟังก์ขันสำหรับวาด
    pyxel.cls(0) # ล้างหน้าต่าง
    pyxel.rect(10, 10, 20, 20, 11) # วาดสี่เหลี่ยมที่ตำแหน่ง X 10 , Y 10 ,ขนาด 20*20 ,สี 11

pyxel.run(update, draw) # รัน