from .geolo import Geologo
class Address(Geologo):
    #este modelo es para representar una dirección de usuario.
    def __init__(self, street, suite, city,zipcode, lat, lng):
        super().__init__(lat, lng) #llamar al constructor de Geolo
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.suite}, {self.city}, {self.zipcode}"