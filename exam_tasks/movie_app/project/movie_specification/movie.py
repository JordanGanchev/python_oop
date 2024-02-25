from abc import ABC, abstractmethod

from project.user import User
from project.utils.validators import validate_non_empty_string, validate_greater_then_value


class Movie(ABC):
    MIN_AGR_RESTRICTION = None

    MIN_YEAR = 1888

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = (
            age_restriction)
            # if age_restriction is not None \
            # else self.DEFAULT_AGR_RESTRICTION
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__validate_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__validate_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.validate_owner(value)
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        self.validate_age_restriction(value)
        self.__age_restriction = value

    @property
    def age_restriction_error_message(self):
        return f"{self.type} movies must be restricted for audience under {self.age_restriction} years!"

    @abstractmethod
    @property
    def type(self):
        pass

    def details(self):
        return f'{self.title} -' \
               f'Title:{self.title},' \
               f'Year:{self.year},' \
               f'Age restriction:{self.age_restriction},' \
               f'Likes:{self.likes},' \
               f'Owned by:{self.owner.username}'

    @staticmethod
    def __validate_title(title):
        validate_non_empty_string(title, "The title cannot be empty string!")

    @classmethod
    def __validate_year(cls, year):
        validate_greater_then_value(year, cls.MIN_YEAR, f"Movies weren't made before {cls.MIN_YEAR}!")

    @staticmethod
    def validate_owner(owner):
        if owner is not User:
            raise ValueError("The owner must be an object of type User!")

    def validate_age_restriction(self, age_restriction):
        validate_greater_then_value(
            age_restriction, self.MIN_AGR_RESTRICTION,
            self.age_restriction_error_message
        )


# self.__class__.__name__ # Dont's every use this

# obj = MyType()
# obj.__class__.__name__ # This is ok