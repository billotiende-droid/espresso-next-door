all_orders = []

class Order:
    def __init__(self,customer, brew, price):
        self.customer = customer
        self.brew = brew
        self.price = price
        all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        from customers import Customers
        if not isinstance(customer, Customers):
            raise TypeError("Customer must be an instance of Customers class")
        self._customer = customer

    @property
    def brew(self):
        return self._brew   

    @brew.setter
    def brew(self, brew):
        from coffee import Coffee
        if not isinstance(brew, Coffee):
            raise TypeError("Brew must be an instance of Coffee class")
        self._brew = brew

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 1.0  or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0 USD")
        self._price = price      





# Example usage:
