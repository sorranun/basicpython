scores = {
    'John': 1200,
    'bobby': 2000,
    'janny': 4200
}

print(scores)
print(scores['bobby'])

# เพิ่มสมาขิกใหม่เข้า dictionary
scores['roger'] = 3200
print(scores)
print('------------------------------------------------')
# การสร้าง Dictioary ว่าง
points = {}

# เพิ่มค่าเข้า Dictionary ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)
print('------------------------------------------------')
# การ loop อ่านสมาชิกของ Dictionary ออกมา
for k, v in scores.items():
    print(k, v)
    print(v)
print('------------------------------------------------')
for k, v in points.items():
    print(k, v)
    print(v)
