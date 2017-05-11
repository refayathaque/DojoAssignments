# Car

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.13 #No parameter needed IF ATTR. HAS VALUE
    def display_all(self):
        if self.price > 10000:
            self.tax = 0.15
        print "Price: $%s, Speed: %s, Fuel: %s, Mileage: %s, Tax: %s" % (self.price, self.speed, self.fuel, self.mileage, self.tax)
        return self

car1 = Car(12000, "130mph", "Full", "15mpg")
car2 = Car(3000, "140mph", "Not Full", "105mpg")
car3 = Car(14000, "150mph", "Full", "76mpg")
car4 = Car(5000, "160mph", "Not Full", "5mpg")
car5 = Car(16000, "170mph", "Full", "89mpg")
car6 = Car(7000, "180mph", "Not Full", "32mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
