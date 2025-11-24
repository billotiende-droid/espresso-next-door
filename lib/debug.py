from customers import Customers
from coffee import Coffee
from orders import Orders
c1 = Customers("Zayn","zayn@hotmail.com")
c2= Customers("Agnes","agnes@gmail.com")
brew = Coffee("Espresso")
brew2 = Coffee("Latte")
order = Orders(c1, brew, 3.5)
order2 = Orders(c2, brew2, 4.0) 


print([order.coffee.brew for order in c1.orders()])  
print(c.brew for c in c1.coffees())
