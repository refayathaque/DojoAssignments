# Bike

class Bike(object):
    def __init__(self, price, max_speed, miles=0): #initial miles is set to be 0
                                                   #whenever a new instance is created.
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def display_info(self):
        print self.price
        print self.max_speed
        print abs(self.miles), "miles" #bc of reversing, ALSO py CONCATENATING
        return self
    def ride(self):
        self.miles += 10 #increase the total miles ridden by 10
        print "Riding : %s miles" % (self.miles) #py INTERPOLATION
        return self
    def reverse(self):
        self.miles -= 5 #decrease the total miles ridden by 5
        print "Reversing : %s miles" % (abs(self.miles))
        return self

bike1 = Bike("$5600", "200mph")
bike2 = Bike("$6000", "220mph")
bike3 = Bike("$6400", "260mph")

bike1.ride().ride().ride().reverse().display_info()
bike2.ride().ride().reverse().reverse().display_info()
bike3.reverse().reverse().reverse().display_info()
