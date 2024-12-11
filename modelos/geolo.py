class Geolo:
    #En este modelo se utilizara para representar las coordenadas de geográficas.
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class Address(Geolo):
    def __init__(self,street, suite, city, zipcode, lat, lng):
        super().__init__(lat, lng)
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode