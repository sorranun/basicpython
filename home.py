# เรียกใช้ Function ใน Package ์Number
#from Number import *

# เรียกใช้และประกาศนามแฝง alias
from Number import number as nb
from Number import calculate as cal

print(nb.factorial(5))
print(cal.plus(3, 5))
