from project.movie_specification.movie import Movie


class Fantasy(Movie):
    MIN_AGR_RESTRICTION = 6
    # AGE_RESTRICTION_VALIDATION_ERROR_MESSAGE = \
    #     f"Fantasy movies must be restricted for audience under {MIN_AGR_RESTRICTION} years!"

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
        age_restriction = age_restriction if age_restriction else self.MIN_AGR_RESTRICTION
        super().__init__(title, year, owner, age_restriction)

    @property
    def type(self):
        return "Fantasy"