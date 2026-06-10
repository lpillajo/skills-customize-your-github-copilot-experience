import unittest

from starter_code import add_numbers, is_even, find_max, divide_numbers


class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-2, 4), 2)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([-5, 0, 5]), 5)

    def test_find_max_empty_list(self):
        with self.assertRaises(ValueError):
            find_max([])

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertAlmostEqual(divide_numbers(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)


if __name__ == "__main__":
    unittest.main()
