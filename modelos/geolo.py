class geolo:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return f"Latitud: {self.lat}, Longitud: {self.lng}"