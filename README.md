# Espresso Next Door - Coffee Shop Orders Management

# Project Overview

This Python project simulates a simple coffee shop order system using object-oriented programming (OOP).
It models three main entities:

Customer – stores customer information and tracks their orders.

Coffee (Brew) – represents a type of coffee and tracks orders for that brew.

Order – represents a purchase made by a customer, linking the customer, brew, and price.

The project emphasizes the single source of truth by maintaining all orders in a centralized all_orders list.

# Features

# Customer Class

Validates name (1–15 characters) and email (must be valid format).

Retrieve all orders for a customer.

Retrieve all unique brews a customer has ordered.

Create a new order.

# Coffee Class (Brew)

Validates brew name (at least 3 characters).

Retrieve all orders for this brew.

Retrieve all unique customers who ordered this brew.

# Order Class

Links a customer, a brew, and a price.

Validates customer type (Customers), brew type (Coffee), and price (1.0–10.0 USD).

Automatically adds each new order to the global all_orders list.

Single Source of Truth

All orders are stored in a single all_orders list, ensuring consistent data across classes.

# Project Structure
espresso-next-door/
│
├── customers.py       # Customer class
├── coffee.py          # Coffee class (brew)
├── orders.py          # Order class and global all_orders list
├── main.py            # Example usage (optional)
└── README.md          # This file

# Getting Started

Clone the repository:

git clone <repository-url>
cd espresso-next-door


# Set up a virtual environment (optional but recommended):

pip install virtualenv
virtualenv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


# Run Python scripts

python3 main.py
