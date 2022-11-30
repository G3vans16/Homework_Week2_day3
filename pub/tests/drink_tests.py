import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennents", 3.00, 2.3)
        self.drink2 = Drink("Kracken and Coke", 2.50, 1)
        self.drink3 = Drink("Mojito", 5.95, 2)
        self.drink4 = Drink("Gin and Tonic", 3.80, 1)
    
    def test_drink_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(3.00, self.drink.price)