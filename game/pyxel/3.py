import pyxel
class App:
	def __init__(self):
		pyxel.init(160, 120, caption='สี่เหลี่ยมจับวงกลม') # (พิกเซลx,พิกเซลy,caption=ชื่อหน้าต่าง)
		self.x = 900 # กำหนดพิกเซส X เริ่มต้นให้วัตถุ
		self.y = 20 # กำหนดพิกเซส Y เริ่มต้นให้วัตถุ
		self.start=0 # ประกาศ start ใช้เก็บสถานะของปุ่มขึ้นลง
		self.startx=0 # ประกาศ startx ใช้เก็บสถานะของปุ่มซ้ายขวา
		pyxel.run(self.update, self.draw)
	def update(self):
		'''
		อัพเดต
		'''
		if pyxel.btnp(pyxel.KEY_Q): # ถ้ากดปุ่ม Q ให้ออก
			pyxel.quit()
		if pyxel.btnp(pyxel.KEY_LEFT): # ถ้ากดปุ่มซ้าย
			self.startx = 1
		elif pyxel.btnp(pyxel.KEY_RIGHT): # ถ้ากดปุ่มวา
			self.startx = 0
		if pyxel.btnp(pyxel.KEY_DOWN): # ถ้ากดปุ่มลง
			self.start = 0
		elif pyxel.btnp(pyxel.KEY_UP): # ถ้ากดปุ่มขึ้น
			self.start = 1
		if self.start==1: # ถ้าสถานะเป็น 1 ให้เลื่อนขึ้น
			self.y = (self.y -1) % pyxel.height
		else: # ให้เลื่อนลง
			self.y  = (self.y + 1) % pyxel.height
		if self.startx==1: # ถ้าสถานะเป็น 1 ให้ไปทางซ้าย
			self.x = (self.x - 1) % pyxel.width
		else: # ให้ไปทางขวา
			self.x = (self.x + 1) % pyxel.width
	def draw(self):
		pyxel.cls(0)
		pyxel.rect(self.x, self.y, self.x + 7, self.y+7, 9)
		
App()