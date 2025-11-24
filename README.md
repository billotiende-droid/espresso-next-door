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

# Class Breakdown

# Coffee Class

Represents a coffee product.

Requirements:

Must accept a name

Name must be at least 3 characters

Uses property getters and setters

# Customers Class

Represents a customer of Espresso Next Door.

Fields:

name — validated (1–15 chars)

email — freely stored

# Special Class Method:

# most_aficionado(coffee)

Returns the customer who has spent the most money on a specific coffee.

# Logic:

Look through all orders in all_orders

Filter orders for the given coffee

Group prices by customer

Sum spending per customer

Return the customer with highest total

Return None if no orders exist

# Order Class
Purpose:

Links:

A Customer

A Coffee

A price

Every new order should append itself to all_orders.

# Features Summary
 Coffee validation

Ensures coffee names are at least 3 letters.

 Customer validation

Names must be within 1–15 characters.

Order tracking

Every order goes into the global all_orders list.

 Spending aggregation

most_aficionado() finds the biggest spender for a specific coffee.

# Fully OOP structured

Uses:

properties

encapsulation

class methods

validation

object relationships

# Future Improvements (optional)

Add unique customer IDs

Add total customer spending method

Add menu with multiple coffee types

Build a CLI interface

Connect to SQLite database.


python3 main.py
