import unittest
from lab04_pokrycieKoduTestami.src.quadratic_equation import QuadraticEquation

class QuadraticEquationTests(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        # arrange
        a, b, c = 0, 2, 4

        # act & assert
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_two_real_roots(self):
        # arrange
        a, b, c = 1, -3, 2
        equation = QuadraticEquation(a, b, c)

        # act
        roots = equation.solve()

        # assert
        self.assertEqual(len(roots), 2)
        self.assertIn(2, roots)
        self.assertIn(1, roots)

    def test_one_real_roots(self):
        # arrange
        a, b, c = 1, -2, 1
        equation = QuadraticEquation(a, b, c)

        # act
        roots = equation.solve()

        # assert
        self.assertEqual(len(roots), 1)
        self.assertEqual(roots[0], 1)

    def test_no_real_roots(self):
        # arrange
        a, b, c = 1, 2, 5
        equation = QuadraticEquation(a, b, c)

        # act
        roots = equation.solve()

        # assert
        self.assertIsNone(roots)

if __name__ == "__main__":
        unittest.main()