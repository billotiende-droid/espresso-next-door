from orders import all_orders

class Coffee:
    def __init__(self,brew):
        self.brew = brew

    @property
    def brew(self):
        return self._brew    
    
    @brew.setter
    def brew(self, brew):
        if not isinstance(brew,str):
            raise TypeError("Brew must be a string")
        if len(brew) < 3 :
            raise ValueError("Brew must be at least 3 characters")
        self._brew = brew


  
    def orders(self):
        coffee_orders = [order for order in all_orders if order.brew == self]
        return coffee_orders
    
    def customers(self):
        unique_customers = [order.customer for order in self.orders()]
        return list(set(unique_customers))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        order_list = self.orders()
        if not order_list:
            return None
        total_price = sum(order.price for order in order_list)
        return total_price / len(order_list)