# import unittest
# from project.team import Team
#
#
# class TestTeam(unittest.TestCase):
#     def setUp(self) -> None:
#         self.team = Team('loko')
#
#     def test_init_method(self):
#         self.assertEqual('loko', self.team.name)
#         self.assertEqual({}, self.team.members)
#
#     def test_name_setter(self):
#         with self.assertRaises(ValueError) as content:
#             self.team.name = '123'
#         self.assertEqual("Team Name can contain only letters!", str(content.exception))
#
#     def test_add_member_if_member_not_exist(self):
#         name_age = {'loko': 3}
#         self.assertEqual(f"Successfully added: loko", self.team.add_member(**name_age))
#         self.assertEqual({'loko': 3}, self.team.members)
#
#     def test_add_member_if_member_exist(self):
#         self.team.members['loko'] = 3
#         name_age = {'loko': 3}
#         self.assertEqual(f"Successfully added: ", self.team.add_member(**name_age))
#         self.assertEqual({'loko': 3}, self.team.members)
#
#     def test_remove_members(self):
#         self.team.members['loko'] = 3
#         self.assertEqual(f"Member loko removed", self.team.remove_member('loko'))
#         self.assertEqual({}, self.team.members)
#
#     def test_remove_member_not_in_members(self):
#         self.team.members['loko'] = 3
#         self.assertEqual(f"Member with name porto does not exist", self.team.remove_member('porto'))
#
#     def test_gt_order_if_true(self):
#         order = Team('loko')
#         self.team.members['cska'] = 2
#         self.team.members['levski'] = 2
#         self.assertTrue(self.team.__gt__(order))
#
#     def test_gt_order_if_false(self):
#         order = Team('loko')
#         order.members['cska'] = 4
#         order.members['levki'] = 5
#         order.members['botev'] = 5
#         self.team.members['cska'] = 2
#         self.team.members['levski'] = 2
#         self.assertFalse(self.team.__gt__(order))
#
#     def test_len_members(self):
#         self.team.members['cska'] = 2
#         self.team.members['levski'] = 2
#         self.assertEqual(2, self.team.__len__())
#
#     #def test_add_method(self):


from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")

    def test_team_init(self):
        team_name = 'Team'
        team = Team(team_name)
        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_raises_when_name_contains_alpha_letters(self):
        with self.assertRaises(ValueError) as context:
            team = Team('123abc.,#@%!')
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member_adds_only_new_players_to_the_team(self):
        self.team.members['ivan'] = 18
        result = self.team.add_member(ivan=18, pesho=21, gosho=19, josh=16)
        self.assertEqual("Successfully added: pesho, gosho, josh", result)
        self.assertEqual(21, self.team.members['pesho'])
        self.assertEqual(19, self.team.members['gosho'])
        self.assertEqual(16, self.team.members['josh'])

    def test_remove_member_return_error_message_when_player_does_not_exist(self):
        member_name = 'gosho'
        result = self.team.remove_member(member_name)
        self.assertEqual(f"Member with name {member_name} does not exist", result)

    def test_remove_member_removes_member_from_the_team(self):
        member_to_remove = 'gosho'
        self.team.members['pesho'] = 21
        self.team.members['gosho'] = 19
        result = self.team.remove_member(member_to_remove)
        self.assertEqual(f"Member {member_to_remove} removed", result)
        self.assertEqual(21, self.team.members['pesho'])
        self.assertTrue(member_to_remove not in self.team.members)

    def test_gt_compares_team_by_members_cont(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19
        another_team = Team('Another')
        another_team.members['member1'] = 21
        another_team.members['member2'] = 22
        another_team.members['member3'] = 23
        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, another_team < self.team)

    def test_len_return_members_count(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19
        self.assertEqual(2, len(self.team))

    def test_add_return_new_team_with_combined_members(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19
        another_team = Team('Another')
        another_team.members['member3'] = 21
        another_team.members['member4'] = 22
        another_team.members['member5'] = 23
        result = self.team + another_team
        expected_result_members = {
            'member1': 18,
            'member2': 19,
            'member3': 21,
            'member4': 22,
            'member5': 23,
        }
        self.assertEqual('TeamAnother', result.name)
        self.assertEqual(expected_result_members, result.members)

    def test_str_returns_members_sorted_in_descending_order_by_age_in_proper_string_format(self):
        self.team.members['member2'] = 19
        self.team.members['member1'] = 18
        self.team.members['member3'] = 20
        result = str(self.team)
        expected = f'Team name: Team\n' + \
                   f'Member: member3 - 20-years old\n' + \
                   f'Member: member2 - 19-years old\n' + \
                   f'Member: member1 - 18-years old'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
