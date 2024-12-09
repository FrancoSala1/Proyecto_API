class company:
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catchPhrse = catchPhrase
        self.bs =bs

    def __str__(self):
        return f"{self.name}, {self.catchPhrse}"