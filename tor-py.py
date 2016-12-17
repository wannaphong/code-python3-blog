# https://python3.wannaphong.com/2016/12/python-ดึงข้อมูลผ่าน-tor.html
import requests
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

resp = requests.get('https://www.facebookcorewwwi.onion/', proxies=proxies)
# แล้วใช้งานตามเอกสาร requests ที่ต้องการ
