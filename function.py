# การสร้างฟังชั่นแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")

# สร้าง function แบบมีการ Return value


def area(width, height):
    total = width*height
    return total


# เรียกใช้งาน function hello()
hello('Sorranun')

# เรียกใช้งาน Function area()
print(area(5, 8))
print(area(15, 8))
print(area(25, 8.9999))


# Function แบบมีค่าเริ่มต้น
def show_info(name='', salary=0.00, lang='not define'):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


# เรียกใช้งาน Function show_info
show_info()
print()
show_info('Samit', 12000, 'PHP')
