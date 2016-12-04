# อ่านทความ https://python3.wannaphong.com/2016/08/%E0%B9%83%E0%B8%8A%E0%B9%89-gnu-octave-%E0%B8%81%E0%B8%B1%E0%B8%9A-python.html
# ใช้ GNU Octave กับ Python
import numpy as np
from oct2py import Oct2Py
oc = Oct2Py()
oc.plot([1,2,3],'-o', linewidth=2)
xx = np.arange(-2*np.pi, 2*np.pi, 0.2)
oc.surf(np.subtract.outer(np.sin(xx), np.cos(xx)))
