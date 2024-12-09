class company:
    # en este se puede representar una compañia asociada a un usuario.
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catchPhrse = catchPhrase
        self.bs =bs

    def __str__(self):
        return f"{self.name}, {self.catchPhrse}"