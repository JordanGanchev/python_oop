import unittest

from project.student_report_card import StudentReportCard


class TestStudentReportCard(unittest.TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard('dan', 12)

    def test_init_element(self):
        self.assertEqual('dan', self.student.student_name)
        self.assertEqual(12, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_setter_name(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_setter_school_year(self):
        with self.assertRaises(ValueError) as content:
            self.student.school_year = 15
        self.assertEqual("School Year must be between 1 and 12!", str(content.exception))

    def test_add_grade_if_not_in_grades_by_subject(self):
        self.student.add_grade('svilen', 5.0)
        self.assertEqual({'svilen': [5.0]}, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.grades_by_subject['svilen'] = []
        self.student.grades_by_subject['svilen'].append(5.00)
        self.student.grades_by_subject['gosho'] = []
        self.student.grades_by_subject['gosho'].append(6.00)
        self.assertEqual('svilen: 5.00'"\n"'gosho: 6.00', self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.student.grades_by_subject['svilen'] = []
        self.student.grades_by_subject['svilen'].append(5.00)
        self.student.grades_by_subject['gosho'] = []
        self.student.grades_by_subject['gosho'].append(6.00)
        self.assertEqual(f"Average Grade: 5.50", self.student.average_grade_for_all_subjects())

    def test_pepr(self):
        self.student.grades_by_subject['svilen'] = []
        self.student.grades_by_subject['svilen'].append(5.00)
        self.student.grades_by_subject['gosho'] = []
        self.student.grades_by_subject['gosho'].append(6.00)

        result = f'Name: dan\n' \
                 f'Year: 12\n' \
                 f'----------\n' \
                 f'svilen: 5.00\n' \
                 f'gosho: 6.00\n' \
                 f'----------\n' \
                 f'Average Grade: 5.50'

        self.assertEqual(result, self.student.__repr__())
