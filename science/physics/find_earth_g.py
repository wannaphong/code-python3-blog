# คำนวณหาค่า g แรงโน้มถ่วงของโลกด้วย Python
# เขียนโดย นาย วรรณพงษ์ ภัททิยไพบูลย์
# https://python3.wannaphong.com/2016/05/หาค่าแรงโน้มถ่วงของโลก.html
from math import pow
import quantities as pq
mass = 5.9723*pow(10,24) * pq.kg
r = 6378.137*pow(10,3) * pq.meter
G = 6.673*pow(10,11) * pq.N*pq.meter**2/ (pq.kg**2)
g = G*mass/r**2
print(g)
