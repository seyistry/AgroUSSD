from product import Product

class Crop(Product):
    def __init__(self, name, category, quantity=0):
        super().__init__(name, category, quantity)
        self.perishable = False

    def set_price(self, price) -> int:
        pass

    def get_price(self, price) -> int:
        pass