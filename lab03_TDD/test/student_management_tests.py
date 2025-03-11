import unittest
from unittest import result

from lab03_TDD.src.student_management import StudentManagement

class StudentManagementTestCase(unittest.TestCase):

    def test_add_student_should_add_student_to_database(self):
        # given
        database = StudentManagement()

        # when
        result = database.add_student("001", "Szymon Lebron", 22)

        # then
        self.assertTrue(result)
        self.assertIn("001", database.students)
        self.assertEqual(database.students["001"], {"name": "Szymon Lebron", "age": 22})

    def test_update_student_should_update_existing_student(self):
        # given
        database = StudentManagement()
        database.add_student("001", "Szymon Lebron", 22)

        # when
        result = database.update_student("001", "Szymon Lebron", 23)

        #then
        self.assertTrue(result)
        self.assertEqual(database.students["001"], {"name": "Szymon Lebron", "age": 23})

    def test_remove_student_should_remove_existing_student(self):
        # given
        database = StudentManagement()
        database.add_student("001", "Szymon Lebron", 22)

        # when
        result = database.remove_student("001")

        # then
        self.assertTrue(result)
        self.assertNotIn("001", database.students)

    def test_add_grade_should_add_grade_to_existing_student(self):
        # given
        database = StudentManagement()
        database.add_student("001", "Szymon Lebron", 22)

        # when
        result = database.add_grade("001", "Matematyka", 2.0)
        result2 = database.add_grade("001", "Fizyka", 6.0)

        # then
        self.assertTrue(result)
        self.assertIn("Matematyka", database.students["001"]["grades"])
        self.assertEqual(database.students["001"]["grades"]["Matematyka"],[2.0])

        self.assertFalse(result2)
        self.assertNotIn("Fizyka", database.students["001"].get("grades", {}))

    def test_avg_grades_should_return_correct_average_for_subject(self):
        # given
        database = StudentManagement()
        database.add_student("001", "Szymon Lebron", 22)
        database.add_student("002", "Bartłomiej Królikowski", 23)

        database.add_grade("001", "Matematyka", 3.0)
        database.add_grade("001", "Matematyka", 4.0)
        database.add_grade("002", "Matematyka", 5.0)

        # when
        result = database.avg_grades("Matematyka")

        # then
        self.assertEqual(result, 4.0)  # (3.0 + 4.0 + 5.0) / 3 = 4.0

    def test_avg_grades_should_return_zero_when_no_grades(self):
        # given
        database = StudentManagement()
        database.add_student("001", "Szymon Lebron", 22)

        # when
        result = database.avg_grades("Matematyka")

        # then
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()