from customers import Customers
from coffee import Coffee
from orders import Orders
customer = Customers("Zayn","zayn@hotmail.com")
brew = Coffee("Espresso")
order = Orders(customer, brew, 3.5)
print(order.customer.name)  # Output: Zayn
print(order.brew.brew)      # Output: Espresso
print(order.price)          # Output: 3.5
