class Customers:
    def __init__(self,name, email):
        if not isinstance(name, str) or not isinstance(email, str):
            raise ValueError("Name and email must be strings.") 
        if len(name) > 15:
            raise ValueError("Name cannot exceed 15 characters.")
        self._name = name
        self._email = email
        self.customers_list = []
       
    def get_customer_name(self):
        return self._name


    def set_customer_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name) > 15:
            raise ValueError("Name cannot exceed 15 characters.")
        self._name = name


    def set_customer_email(self, email):
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        self._email = email



customers = [ 
Customers("Boni","boni@hotmail.com"),
Customers("Musa","musa@gmail.com"),
Customers("Zayn","zayn@gmail.com"),
Customers("Mbuthia","mbuthia@total.com"),
Customers("Eugine","eugo@hotmail.com"),
Customers("Agnes","agi@hotmail.com"),
Customers("Lucy","lucy@hotmail.com")
]

print(customers[3].get_customer_name())