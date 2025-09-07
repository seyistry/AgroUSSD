from product import Product

class Crop(Product):
    def __init__(self, name, price, quantity, crop_type: str, measurement_unit: str, location: str):
        super().__init__(name, price, quantity)
        self.crop_type = crop_type # could be grain, tuber, etc...
        self.measurement_unit = measurement_unit
        self.location = location

    def change_price(self, new_price: int) -> int:
        self.price = new_price

    def update_quantity(self, quantity_sold: int) -> bool:
        if quantity_sold <= self.quantity:
            self.quantity -= quantity_sold
            return True
        return False
    
    def is_available(self) -> bool:
        if self.quantity == 0:
            return False
        return True