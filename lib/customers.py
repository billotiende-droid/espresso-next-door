from orders import all_orders

class Customers:
    def __init__(self,name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email,str):
            raise TypeError("Email must be a string")
        if "@" not in email or "." not in email:
            raise ValueError("Email must be a valid email address")
        self._email = email    

    def orders(self):
        customer_orders = [order for order in all_orders if order.customer == self]
        return customer_orders    
    
    def coffees(self):
        unique_coffees = [order.brew for order in self.orders()]
        return list(set(unique_coffees))
    
    def create_order(self, brew, price):
        from orders import Order
        new_order = Order(self, brew, price)
        return new_order
    
    @classmethod
    def most_aficionado(cls,coffee):
        coffee_orders = [order for order in all_orders if order.brew == coffee]

        if not coffee_orders:
            return None
        
        spending = {}
        
        for order in coffee_orders:
            customer = order.customer

            price = order.price

            if customer in spending:
                spending[customer] = 0
            spending[customer] += price   

        return max(spending, key=lambda customer: spending[customer])     




        