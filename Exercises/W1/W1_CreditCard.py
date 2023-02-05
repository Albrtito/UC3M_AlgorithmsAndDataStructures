class CreditCard:
    def __init__(self, customer, idCard, limit):
        self._customer = customer
        self._idCard = idCard
        self._limit = limit
        self._balance = 0
    """
    # properties
    @property
    def customer(self):
        return self._customer
    @property
    def idCard(self):
        return self._idCard
    @property
    def _limit(self):
        return self._limit

    def _balance(self):
        return self._balance
    """
    # operators

    def charge(self, price):
        enough_money = True
        if price > self._balance:
            enough_money = False
        else:
            self._balance -= price
        return enough_money

    def make_deposit(self, amount):
        self._balance += amount
        return self._balance


card_1 = CreditCard(89, 2340, 245)
print(card_1.charge(89))
print(card_1.charge(100000))
print(card_1.make_deposit(34000))
print(card_1._balance)
