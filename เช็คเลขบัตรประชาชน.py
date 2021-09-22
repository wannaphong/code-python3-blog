# เขียนโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
# https://python3.wannaphong.com/2016/07/เช็คความถูกต้องเลขบัตร.html
# วิธีใช้
# จะคืนค่า True หากถูกต้อง
# จะคืนค่า False หากไม่ถูกต้อง
def checkPID(pid):
	pid = pid.strip()	# บางกรณีเกิดมีการใส่ space หน้า-หลัง
	thai_num = "๐๑๒๓๔๕๖๗๘๙"
	if(len(pid) != 13): # ถ้า pid ไม่ใช่ 13 ให้คืนค่า False
		return False
	if not(pid.isdigit()):	# ตรวจสอบกว่าเป็นตัวเลขมั้ย ลดการทำงานในขั้นตอนด้านล่าง
		return False
	if pid[0] in thai_num:	# เจอเคสการใช่เลขไทย
		return False
	
	num=0 			# ค่าสำหรับอ้างอิง index list ข้อมูลบัตรประชาชน
	num2=13 		# ค่าประจำหลัก
	listdata=list(pid) 	# list ข้อมูลบัตรประชาชน
	sum=0 			# ผลลัพธ์
	while num<12:
		sum+=int(listdata[num])*(num2-num) 	# นำค่า num เป็น  index list แต่ละตัว *  (num2 - num) แล้วรวมเข้ากับ sum
		num+=1 		# เพิ่มค่า num อีก 1
	digit13 = sum%11 	# sum หาร 11 เอาเศษ
	if digit13==0: 		# ถ้าเศษ = 0
		digit13=1 	# ค่าหลักที่ 13 คือ 1
	elif digit13==1: 	# ถ้าเศษ = 1
		digit13=0 	# ค่าหลักที่ 13 คือ 0
	else:
		digit13=11-digit13  	# ถ้าเศษไม่ใช่กับอะไร ให้เอา 11 - digit13
	if digit13==int(listdata[12]): 	# ถ้าค่าหลักที่ 13 เท่ากับค่าหลักที่ 13 ที่ป้อนข้อมูลมา คืนค่า True
		return True
	else: 			# ถ้าค่าหลักที่ 13 ไม่เท่ากับค่าหลักที่ 13 ที่ป้อนข้อมูลมา คืนค่า False
		return False
