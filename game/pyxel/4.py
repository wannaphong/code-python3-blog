import pyxel
from random import randint
class App:
	def __init__(self):
		pyxel.init(160, 120, caption='สี่เหลี่ยมจับวงกลม') # (พิกเซลx,พิกเซลy,caption=ชื่อหน้าต่าง)
		self.x = 900 # กำหนดพิกเซส X เริ่มต้นให้วัตถุ
		self.y = 20
		self.score = 0 # ประกาศตัว score ใช้เก็บคะแนน
		self.start=0
		self.startx=0
		pyxel.run(self.update, self.draw)
	def update(self):
		'''
		อัพเดต
		'''
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		if pyxel.btnp(pyxel.KEY_LEFT):
			self.startx = 1
		elif pyxel.btnp(pyxel.KEY_RIGHT):
			self.startx = 0
		if pyxel.btnp(pyxel.KEY_DOWN):
			self.start = 0
		elif pyxel.btnp(pyxel.KEY_UP):
			self.start = 1
		if self.start==1:
			self.y = (self.y -1) % pyxel.height
		else:
			self.y  = (self.y + 1) % pyxel.height
		if self.startx==1:
			self.x = (self.x - 1) % pyxel.width
		else:
			self.x = (self.x + 1) % pyxel.width
	def draw(self):
		pyxel.cls(0)
		pyxel.rect(self.x, self.y, self.x + 7, self.y+7, 9)
		s = 'SCORE {:>4}'.format(self.score)
		pyxel.text(5, 4, s, 1)
		pyxel.text(4, 4, s, 7)
		
App()