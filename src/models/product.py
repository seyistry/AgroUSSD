from abc import ABC, abstractmethod

# Base class for crops, livestock and processed goods
class Product:
    def __init__(self, name, category, quantity= 0):
        self.name = name
        self.category = category
        self.quantity = quantity

    @abstractmethod
    def set_price(self, price) -> int:
        pass

    def get_price(self, price) -> int:
        pass