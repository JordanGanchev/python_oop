import unittest
from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis = TennisPlayer('roger', 50, 10)

    def test_init_method(self):
        self.assertEqual('roger', self.tennis.name)
        self.assertEqual(50, self.tennis.age)
        self.assertEqual(10, self.tennis.points)
        self.assertEqual([], self.tennis.wins)

    def test_setter_name(self):
        with self.assertRaises(ValueError) as content:
            self.tennis.name = 'rt'
        self.assertEqual("Name should be more than 2 symbols!", str(content.exception))

    def test_setter_age(self):
        with self.assertRaises(ValueError) as content:
            self.tennis.age = 16
        self.assertEqual("Players must be at least 18 years of age!", str(content.exception))

    def test_add_new_win_if_wins_dont_amount(self):
        self.tennis.add_new_win('bul')
        self.assertEqual(['bul'], self.tennis.wins)

    def test_add_new_win_if_wins_is_amount(self):
        self.tennis.wins.append('bul')
        self.assertEqual(f"bul has been already added to the list of wins!", self.tennis.add_new_win('bul'))

    def test__lt__method(self):
        # Create another instance of TennisPlayer
        other = TennisPlayer('grishu', 30, 15)

        # Call the __lt__ method on the current instance (self) and pass the other instance as an argument
        result = self.__lt__(other)

        # Determine the expected result based on the logic of your __lt__ method
        expected_result = f'grishu is a top seeded player and he/she is better than grishu'

        # Assert that the result matches the expected output
        self.assertEqual(expected_result, result)


#---------------------------------------------------------------------------

from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayerClass(TestCase):
    def test_correct_init(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.assertEqual(self.tennis_player.name, "Alex")
        self.assertEqual(self.tennis_player.age, 20)
        self.assertEqual(self.tennis_player.points, 0)
        self.assertEqual(self.tennis_player.wins, [])

    def test_shorter_name__should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('Al', 20, 0)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_younger_age__should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('Alex', 17, 0)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win__not_existing__should_add_successfully(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.add_new_win('Australian Open 2023')
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023'])

        result = self.tennis_player.add_new_win('French Open 2022')
        self.assertIsNone(result)
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023', 'French Open 2022'])

    def test_add_new_win_with_existing_win__should_not_add(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.add_new_win('Australian Open 2023')
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023'])

        result = self.tennis_player.add_new_win('Australian Open 2023')
        self.assertEqual(result, "Australian Open 2023 has been already added to the list of wins!")
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023'])

    def test__lt__should_return_first_player_is_better(self):
        self.tennis_player = TennisPlayer('Alex', 20, 1520)
        self.other_player = TennisPlayer('Grigor', 30, 1519)

        result = self.tennis_player < self.other_player
        self.assertEqual(result, "Alex is a better player than Grigor")

    def test__lt__should_return_other_player_is_better(self):
        self.tennis_player = TennisPlayer('Alex', 20, 1519)
        self.other_player = TennisPlayer('Grigor', 30, 1520)

        result = self.tennis_player < self.other_player
        self.assertEqual(result, "Grigor is a top seeded player and he/she is better than Alex")

    def test__str__no_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.assertEqual(self.tennis_player.wins, [])

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: ')

    def test__str__one_win(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023')

    def test__str__two_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023', 'FO 2022']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023, FO 2022')


if __name__ == '__main__':
    main()