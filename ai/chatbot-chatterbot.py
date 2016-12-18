# สร้าง Machine Learning โต้ตอบสนทนาด้วย ChatterBot ในภาษาไพทอน
# https://python3.wannaphong.com/2015/10/สร้าง-machine-learning-โต้ตอบสนทนา-python.html
__author__ = 'วรรณพงษ์'
from chatterbot import ChatBot


bot = ChatBot("Training Bot Example",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
    io_adapter="chatterbot.adapters.io.TerminalAdapter",
    database="th_database.db") # กำหนดค่า ฐานข้อมูลในนี้คือ th_database.db หากไม่มี ระบบจะทำการสร้างใหม่

'''
ให้ Bot พูดคุยสนทนาง่าย ๆ เพื่อช่วยให้มันได้เรียนรู้วิธีการตอบสนองต่อคำสั่งอื่น
กดปุ่ม ctrl-c หรือ ctrl-d เพื่อออกจากการสนทนา
'''
training_data = [
    "สวัสดีค่ะ",
    "ทำอะไรอยู่ค่ะ",
    "กำลังรอคำสั่งจากท่านค่ะ",
    "คุณเป็นใคร",
    "กินข้าวยัง",
    "ค่ะ"
]

bot.train(training_data)

user_input = ""

while True:
    try:
        user_input = bot.get_input() # รับข้อความผู้ใช้
        bot_input = bot.get_response(user_input) # ดึงข้อมูล
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
