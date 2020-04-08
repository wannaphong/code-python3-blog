# บทความ https://python3.wannaphong.com/2020/04/pdf-pdfbox-python.html
import pdfbox
p = pdfbox.PDFBox()
p.extract_text('situation-no95-070463.pdf',output = "data.txt") # ดึงออกมาเป็นไฟล์ txt ชื่อ data.txt
p.pdf_to_images('situation-no95-070463.pdf') # แปลง pdf แต่ละหน้าเป็นรูปภาพ
p.extract_images('situation-no95-070463.pdf') # ดึงภาพจาก PDF
