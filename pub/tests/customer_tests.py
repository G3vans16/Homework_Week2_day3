import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Gareth", 20.00, 30, 0)
        self.customer2 = Customer("John", 100.00, 17, 0)
        self.customer3 = Customer("Bob", 50.00, 17, 25.00)

    def test_customer_name(self):
        self.assertEqual("Gareth", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_buy_drink(self):
        drink = Drink("Tennents", 3.00, 2.3)
        self.customer.buy_drink(drink)
        self.assertEqual(17.00, self.customer.wallet)

    def test_buy_drink_from_pub(self):
        drink = Drink("Tennents", 3.00, 2.3)
        pub = Pub("The Boiler Plate", 1000.00)
        # self.customer.buy_drink(drink)
        # pub.sell_drink(drink)
        self.customer.buy_drink_from_pub(pub, drink)
        self.assertEqual(17.00, self.customer.wallet)
        self.assertEqual(1003.00, pub.till)

    def test_drunkenness(self):
        drink = Drink("Tennents", 3.00, 2.3)
        self.customer.increase_drunkenness(drink)
        self.assertEqual(2.3, self.customer.drunkenness)