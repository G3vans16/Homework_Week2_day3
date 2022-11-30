class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def sell_drink(self, drink):
        self.till += drink.price
        # self.drinks.remove(drink)

    def id_customer(self, customer):
        if customer.age >= 18:
            return True
        else: return False

    def sell_drink_to_customer(self, drink, customer, pub):
        if self.id_customer(customer) and self.check_drunkenness(customer) == True:
            customer.buy_drink_from_pub(pub, drink)

    def check_drunkenness(self, customer):
        if customer.drunkenness <= 23.00:
            return True
        else: return False