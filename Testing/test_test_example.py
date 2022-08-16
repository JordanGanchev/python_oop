from unittest import TestCase

from python_oop.Testing.test_example import Person

# Triple A - Arrange, Act, Assert

count = 0


class TestPerson(TestCase):
    FIRST_NAME = 'dancho'
    LAST_NAME ='ganchev'
    AGE = 19

    def setup(self) -> None:
        self.person = Person(self.FIRST_NAME, self.LAST_NAME, self.AGE)

    def test_fullname__expect_to_be_correct(self):

        global count
        count += 3
        print(count)

        # Arrange
        person = Person("Dancho", "Ganchev", 34)

        # Act
        actual_fullname = person.fullname

        # naming: act__arrange__assert for test

        # Assetr
        expected_fullname = 'dancho Ganchev'

        self.assertEqual(actual_fullname, expected_fullname)

    def test_get_info__expect_to_be_correct(self):
        global count
        count += 4
        print(count)

        person = Person('Doncho', 'Minkov', 20)

        actual_info = person.get_info()
        expected_info = 'Doncho Mincov is 20'

        self.assertEqual(expected_info, actual_info)