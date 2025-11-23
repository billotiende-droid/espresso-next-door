class Orders:
    def __init__(self,customer, brew, price):
        self.customer = customer
        self.brew = brew
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        from lib.customers import Customers
        if not isinstance(customer, Customers):
            raise TypeError("Customer must be an instance of Customers class")
        self._customer = customer

    @property
    def brew(self):
        return self._brew   

    @brew.setter
    def brew(self, brew):
        from lib.coffee import Coffee
        if not isinstance(brew, Coffee):
            raise TypeError("Brew must be an instance of Coffee class")
        self._brew = brew        