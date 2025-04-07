from lab06_codeSmell.project_NASA.BasicLunarRover import BasicLunarRover
import unittest

class TestBasicLunarRover(unittest.TestCase):

    def test_initialization(self):
        rover = BasicLunarRover()
        self.assertEqual(rover.get_position(), (0, 0))
        self.assertEqual(rover.get_orientation(), 'N')

    def test_move_forward(self):
        rover = BasicLunarRover()
        rover.move_forward(3)
        self.assertEqual(rover.get_position(), (0, 3))

    def test_move_backward(self):
        rover = BasicLunarRover()
        rover.move_backward(2)
        self.assertEqual(rover.get_position(), (0, -2))

    def test_rotate_left(self):
        rover = BasicLunarRover()
        rover.rotate_left()
        self.assertEqual(rover.get_orientation(), 'W')
        rover.rotate_left()
        self.assertEqual(rover.get_orientation(), 'S')

    def test_rotate_right(self):
        rover = BasicLunarRover()
        rover.rotate_right()
        self.assertEqual(rover.get_orientation(), 'E')
        rover.rotate_right()
        self.assertEqual(rover.get_orientation(), 'S')

    def test_complex_movement(self):
        rover = BasicLunarRover()
        rover.move_forward(2)    # (0, 2), N
        rover.rotate_right()     # E
        rover.move_forward(3)    # (3, 2), E
        rover.rotate_left()      # N
        rover.move_backward(1)   # (3, 1), N
        self.assertEqual(rover.get_position(), (3, 1))
        self.assertEqual(rover.get_orientation(), 'N')

    def test_invalid_orientation(self):
        with self.assertRaises(ValueError):
            BasicLunarRover(start_orientation='X')  # Niepoprawna orientacja

    def test_negative_steps(self):
        rover = BasicLunarRover()
        with self.assertRaises(ValueError):
            rover.move_forward(-1)
        with self.assertRaises(ValueError):
            rover.move_backward(-5)

if __name__ == "__main__":
    unittest.main()
