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
        from orders import all_orders
        coffee_orders = [order for order in all_orders if order.brew == self]
        return coffee_orders
    
   