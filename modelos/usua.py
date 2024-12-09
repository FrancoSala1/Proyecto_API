from modelos.address import address
from modelos.compañia import compañia

class User:
# Aqui se representara a un usuario.
    def __init__(self, id, nombre, username, email, address, celular, website, compañia):
        self.id = id
        self.nombre = nombre
        self.username = username
        self.email = email
        self.address = address
        self.celular = celular
        self.website = website
        self.compañia = compañia(**compañia)

    def __str__(self):
        return f"Usuario: {self.name} ({self.usermane}), Email: {self.email}"