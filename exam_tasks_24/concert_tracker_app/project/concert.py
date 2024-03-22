class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in  ["Metal", "Rock", "Jazz"]:
            raise ValueError
        self.__genre = value


