class Customers:
    def __init__(self,name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self.name = name
    

        