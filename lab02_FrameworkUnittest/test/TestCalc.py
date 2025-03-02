from lab02_FrameworkUnittest.src.Calc import Calc
import unittest

class TestCalc(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.calc = Calc()


    def test_add(self):
        print("** test_add()")

        # Arrange
        a, b = 3,2
        expected = 5

        # Act
        result = self.calc.add(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_substract(self):
        print("** test_substract()")

        # Arrange
        a,b = 10,4
        expected = 6

        # Act
        result = self.calc.substract(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_divide_by_zero(self):
        print("** test_divide_by_zero()")

        # Arrange
        a, b = 10, 0

        #Act & Assert
        with self.assertRaises(ValueError):
            self.calc.divide(a, b)


    def tearDown(self):
        print("** tearDown()")
        self.calc = None

if __name__ == '__main__':
    unittest.main()