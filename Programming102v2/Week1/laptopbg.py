class Laptopbg():
    class Product:

        def __init__(self, name, bought_for, selling_price):
            self.name = name
            self.bought_for = bought_for
            self.selling_price = selling_price

        def profit(Product):
            return (Product.selling_price - Product.bought_for)

    class Laptop(Product):

        def __init__(self, name, bought_for, selling_price, hdd, ram):
            super().__init__(name, bought_for, selling_price)
            self.hdd = hdd
            self.ram = ram

    class Smartphone(Product):

        def __init__(self, name, bought_for, selling_price, display_size, mega_pixels):
            super().__init__(name, bought_for, selling_price)
            self.display_size = display_size
            self.mega_pixels = mega_pixels

    class Store:

        def __init__(self, name):
            self.name = name
            self.dict_of_products = {}
            self.cash = 0

        def load_new_products(self, product, count):
            if product in self.dict_of_products:
                self.dict_of_products[product] += count
                self.cash -= self.dict_of_products[product].bought_for
            else:
                self.dict_of_products[product] = count
                self.cash -= product.bought_for

        def list_products(self):
            for item in self.dict_of_products:
                print("{} - {} count".format(item.name, self.dict_of_products[item]))

        def sell_product(self, product):
            if product.name in self.dict_of_products:
                self.dict_of_products[product.name] -= 1
                self.cash += self.dict_of_products[product].selling_price
                print (True)
            else:
                print (False)

        def total_income(self):
            return ("Your profit is {}".format(self.cash))

    new_laptop = Laptop("HP HackBook", 1000, 2000, 1000, 8096)
    new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    another_smartphone = Smartphone('Mac Phone', 500, 820, 7, 10)
    new_store = Store('Laptop.bg')
    new_store.load_new_products(new_smarthphone, 20)
    new_store.load_new_products(new_laptop, 203)
    new_store.load_new_products(another_smartphone, 2043)
    new_store.list_products()
    print(new_store.sell_product(new_smarthphone))
    new_store.list_products()
    new_store.total_income
