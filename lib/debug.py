from customers import Customers
from coffee import Coffee
from orders import Order

# Example usage:
zayn = Customers("Zayn","zayn@gmail.com")
agnes = Customers("Agnes","agnes@hotmail.com")


espresso = Coffee("Espresso")
latte = Coffee("Latte")

Orderr1 = Order(zayn, espresso, 3.5)
Orderr2 = Order(agnes, latte, 4.0)
Orderr3 = Order(zayn, latte, 4.5)


# customer queries
print([order.brew.brew for order in zayn.orders()])  # Output: ['Espresso', 'Latte']
print([brew.brew for brew in zayn.coffees()])    # Output: ['Espresso', 'Latte']

# coffee queries
print([coffee.name for coffee in latte.customers()])  # Output: ['Agnes', 'Zayn']
print([coffee.name for coffee in espresso.customers()])  # Output: ['Zayn']

# access order details
print(Orderr1.customer.name)  # Output: Zayn
print(Orderr1.brew.brew)      # Output: Latte
print(Orderr1.price)          # Output: 3.5