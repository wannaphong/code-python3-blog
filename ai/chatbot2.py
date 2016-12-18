# ทำ Chat Bot ง่าย ๆ ในภาษา Python
# เขียนโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
#  https://python3.wannaphong.com/2015/07/ทำ-chat-bot-ง่าย-ๆ-ในภาษา-python.html
import random
while True:
	text = input("> ")
	a = ['HI','Hello']
	b = ['Hello :D','Hi',':D']
	if text in a:
		print(random.choice(b))
	else:
		print("?")
