import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Boiler Plate", 1000.00)
    
    def test_pub_name(self):
        self.assertEqual("The Boiler Plate", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_sell_drink(self):
        drink = Drink("Tennents", 3.00, 2.3)
        self.pub.sell_drink(drink)
        self.assertEqual(1003.00, self.pub.till)

    def test_id_customer_old_enough(self):
        customer = Customer("Gareth", 20.00, 30, 0)
        self.pub.id_customer(customer)
        self.assertEqual(True, self.pub.id_customer(customer))

    def test_id_customer_not_old_enough(self):
        customer = Customer("John", 100.00, 17, 0)
        self.pub.id_customer(customer)
        self.assertEqual(False, self.pub.id_customer(customer))

    def test_sell_drink_to_customer_above_18(self):
        customer = Customer("Gareth", 20.00, 30, 0)
        drink = Drink("Kracken and Coke", 2.50, 1)
        self.pub.sell_drink_to_customer(drink, customer, self.pub)
        self.assertEqual(17.50, customer.wallet)

    def test_sell_drink_to_customer_underage(self):
        customer = Customer("John", 100.00, 17, 0)
        drink = Drink("Kracken and Coke", 2.50, 1)
        self.pub.sell_drink_to_customer(drink, customer, self.pub)
        self.assertEqual(100.00, customer.wallet)

    def test_check_drunkenness_level_pass(self):
        customer = Customer("Gareth", 20.00, 30, 0)
        self.pub.check_drunkenness(customer)
        self.assertEqual(True, self.pub.check_drunkenness(customer))

    def test_check_drunkenness_level_fail(self):
        customer = Customer("Bob", 50.00, 17, 25.00)
        self.pub.check_drunkenness(customer)
        self.assertEqual(False, self.pub.check_drunkenness(customer))

    def test_sell_drink_to_customer_not_drunk(self):
        customer = Customer("Gareth", 20.00, 30, 0)
        drink = Drink("Kracken and Coke", 2.50, 1)
        self.pub.sell_drink_to_customer(drink, customer, self.pub)
        self.assertEqual(17.50, customer.wallet)

    def test_sell_drink_to_customer_drunk(self):
        customer = Customer("Bob", 50.00, 17, 25.00)
        drink = Drink("Kracken and Coke", 2.50, 1)
        self.pub.sell_drink_to_customer(drink, customer, self.pub)
        self.assertEqual(50.00, customer.wallet)