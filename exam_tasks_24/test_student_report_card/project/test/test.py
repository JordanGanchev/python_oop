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
