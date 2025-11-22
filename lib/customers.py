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

    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email,str):
            raise TypeError("Email must be a string")
        if "@" not in email or "." not in email:
            raise ValueError("Email must be a valid email address")
        self._email = email    
    

        