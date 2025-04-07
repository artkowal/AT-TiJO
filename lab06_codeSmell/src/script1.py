from collections import Counter
import unittest


def lottery(numbers, n):
    """
    Zwraca listę elementów, które występują w sekwencji `numbers` dokładnie `n` razy.
    Jeśli `numbers` jest puste lub `n < 1`, zwracana jest pusta lista.
    """
    if not numbers or n < 1:
        return []

    counts = Counter(numbers)
    return [elem for elem, count in counts.items() if count == n]


class TestLotteryFunction(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(lottery([1, 1, 3, 2, 2, 2, 4, 5], 2), [1])
        self.assertEqual(lottery([1, 1, 2, 2, 2, 3, 4, 5], 3), [2])
        self.assertCountEqual(lottery([1, 2, 2, 2, 3, 4, 5, 5, 1], 2), [1, 5])

    def test_empty_list(self):
        self.assertEqual(lottery([], 1), [])

    def test_n_zero_or_negative(self):
        self.assertEqual(lottery([1, 2, 3], 0), [])
        self.assertEqual(lottery([1, 2, 3], -1), [])

    def test_no_element_meets_criteria(self):
        self.assertEqual(lottery([1, 1, 3, 2, 2, 2, 4, 5], 7), [])

    def test_none_input(self):
        self.assertEqual(lottery(None, 2), [])


if __name__ == "__main__":
    unittest.main()
