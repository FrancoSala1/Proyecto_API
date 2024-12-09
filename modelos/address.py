class address:
    def __init__(self, street, suite, city,zipcode):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.suite}, {self.city}, {self.zipcode}"