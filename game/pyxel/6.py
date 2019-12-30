import pyxel
from random import randint
class App:
	def __init__(self):
		pyxel.init(160, 120, caption='สี่เหลี่ยมจับวงกลม') # (พิกเซลx,พิกเซลy,caption=ชื่อหน้าต่าง)
		self.x = 900 # กำหนดพิกเซส X เริ่มต้นให้วัตถุสี่เหลี่ยม
		self.y = 20 # กำหนดพิกเซส Y เริ่มต้นให้วัตถุสี่เหลี่ยม
		self.x2 = 90  # x สำหรับวงกลม
		self.y2 = 100  # y สำหรับวงกลม
		self.score = 0
		self.start=0
		self.startx=0
		a = 'c3e2g2c3 e2g2c3e2' # code เสียง
		b = 'c3d2g2c3 d2g2c3d2'
		pyxel.sound(0).set(a * 3 + b * 1, 't', '2', 'f', 30)
		pyxel.play(0, 0, loop=True) # เล่นเสียง
		pyxel.run(self.update, self.draw)
	def get_c(self):
		x=[self.x2-i for i in range(6)]
		x.extend([self.x2+i for i in range(6)])
		y=[self.y2-i for i in range(6)]
		y.extend([self.y2+i for i in range(6)])
		return (x,y)
	def update(self):
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
		tt=self.get_c()
		if self.x in tt[0] and self.y in tt[1]: # กรณีที่จับวงกลมได้
			self.score+=1 # บวกแต้มเพิ่มอีก 1
			self.x2=randint(0, 160) # สุ่มค่า x2 ของวงกลมใหม่
			self.y2=randint(0, 120) # สุ่มค่า x1 ของวงกลมใหม่
	def draw(self):
		pyxel.cls(0)
		pyxel.circ(self.x2, self.y2, 6, 6) # วาดวงกลม (x,y,รัศมี,สี)
		pyxel.rect(self.x, self.y, self.x + 7, self.y+7, 9)
		s = 'SCORE {:>4}'.format(self.score)
		pyxel.text(5, 4, s, 1)
		pyxel.text(4, 4, s, 7)
		
App()