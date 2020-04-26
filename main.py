# import ทั้งหมดทุก function ใน Module
#import numbers

# import มาบาง function
#from numbers import factorial

# import ทุกฟังชั่น (ใช้บ่อยๆ)
from numbers import *

# importและเปลี่ยนชื่อฟังชั่น(นามแฝง) alias
from numbers import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

print(factorial(5))
print(fibonacci(100))

print(fa(5))
print(fi(100))
