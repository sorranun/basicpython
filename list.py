number = [5, 8, 13, 24, 7, 16]
name = ['Jone', 'jane', 'Jany', 'Wasan']
mixed = [10, 25.75, True, "Samit"]

# การเข้าถึงสมาชิกใน List
print(number[1])
print(name[3])
print(mixed[1], mixed[3])
print(number)

# การนับจำนวนสมาชิกใน List
print("สมาชิกทั้งหมดของ number=", len(number))

# การสร้าง List แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกเข้าไปใน list ว่าง
data.append(10)
data.append(15)
data.append(20)

print(data)

# การ update สมาชิกใน list
data[1] = 12
print(data)

# function วนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print(n)

# Loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num
print(sum)
