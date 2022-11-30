class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def buy_drink_from_pub(self, pub, drink):
        self.wallet -= drink.price
        pub.till += drink.price

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level

    