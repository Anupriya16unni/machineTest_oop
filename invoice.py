class Invoice:
    def __init__(self, part_number, part_description, quantity, price):
        self.__number = part_number
        self.__description = part_description
        self.__quantity = quantity
        self.__price = price

    def display_details(self):
        print("part number =", self.__number)
        print("part description =", self.__description)
        print("quantity of the item being purchased =", self.__quantity)
        print("price per item =", self.__price)
        
    def get_number(self):
        print(self.__number) 

    def get_description(self):
        print(self.__description)

    def get_quantity(self):
        print(self.__quantity)

    def get_price(self):
        print(self.__price)

    def set_number(self,new_number):
        self.__number=new_number
    
    def set_description(self,new_description):
        self.__description=new_description

    def set_quantity(self,new_quantity):
        self.__quantity=new_quantity

    def set_price(self,new_price):
        self.__price=new_price

    def get_invoice(self):
        if self.__quantity<0:
            self.__quantity=0
        elif self.__price<0:
            self.__price=0
        print("Amount : ",self.__quantity*self.__price)

invoice1 = Invoice(3, "good product", 4 , 500)
invoice1.get_invoice()
invoice1.display_details()