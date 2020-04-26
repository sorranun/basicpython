a = 3
b = 4.92
c = "itgenius"
print(a)
print(b)
print(c)

#  การสร้างตัวแปรหลายตัวในบรรทัดเดียวกัน
x = y = z = 10
print(x, y, z)
j, k = 5, 15
print(j, k)

# Boolean
status = True
msg = False
print(status, msg)

# ตัีวแปรแสดงผลร่วมกับตัวแปร
# วิธีที่ 1 concat string
print("ราคาขายต่อชิ้่น", b, 'บาท')

# วิธีที่ 2 string interploation
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3 format string (นิยมใช้แบบนี้)
b = 3.14
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
