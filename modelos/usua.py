from .address import Address
from .company import Company

class User(Address, Company):
# Aqui se representara a un usuario.
    def __init__(self, id, nombre, username, email, calle, cuidad, address, celular, suite, website, zipcode, company, lat, lng, nombre_compañia, cath_phrase, bs):
        #llamar a los constructores de las clases.
        Address.__init__(self, calle, suite, cuidad, zipcode, lat, lng)
        Company.__init__(self, nombre_compañia, cath_phrase, bs)
        self.id = id
        self.nombre = nombre
        self.username = username
        self.email = email
        self.address = address
        self.celular = celular
        self.website = website
        self.compañia = Company(**Company)

    def __str__(self):
        return f"Usuario: {self.name} ({self.usermane}), Email: {self.email}"