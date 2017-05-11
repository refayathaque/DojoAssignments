# Product

class Product(object):

    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale" #naming and passing DEFAULT parameters, not included ^

    def sell(self):
        self.status = "sold"
        return self

    def tax(self, tax_rate):
        self.price *= (1 + tax_rate)
        return self

    def return_item(self, return_reason):
        if return_reason == "defective":
            self.status = "defective"
            self.price = 0
        elif return_reason == "unopened":
            self.status = "for sale"
        elif return_reason == "opened":
            self.status = "used"
            self.price *= 0.8
        return self

    def display_info(self):
        print self.price, " - Price"
        print self.item_name, " - Item"
        print self.weight, " - Weight"
        print self.brand, " - Brand"
        print self.cost, " - Cost"
        print self.status, " - Status"
        print "*" * 20
        return self

product1 = Product(33, "Cap", 88, "New Era", 23)
product2 = Product(72, "Shirt", 24, "Hanes", 6)
product3 = Product(14, "Chips", 88, "Cheetos", 3)
product4 = Product(50, "Headphones", 24, "Sony", 66)
product5 = Product(16, "Paper", 88, "Mead", 2)
product6 = Product(51, "Monitor", 24, "Asus", 91)

# Instantiation
product1.sell().display_info()
product2.tax(0.3).display_info() #tax_rate is wtv we pass
product3.return_item("defective").display_info() #works! price is 0!
product4.display_info()
product5.display_info()
product6.tax(0.4).return_item("opened").display_info() #works! price reflects tax AND return_item!
