class Car:
    # Properties
    color = ""
    brand = ""
    number_of_wheel = 4
    number_of_seats = 4
    maxspeed = 0

    # Constructor
    def __init__(self, color, brand, number_of_wheel, number_of_seats, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheel = number_of_wheel
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed
    # Create method set color

    def setcolor(self, x):
        self.color = x

    def setbrand(self, xx):
        self.brand = xx

    def setmaxspeed(self, xxx):
        self.maxspeed = xxx

    def printdata(self):
        print("Color of This car id", self.color)
        print("Brand of This car id", self.brand)
        print("Maxspeed of This car id", self.maxspeed)

    # Deconstructor

    def __del__(self):
        print()
