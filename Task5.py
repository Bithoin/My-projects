import unittest
class IntegerSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)


class TestIntegerSet(unittest.TestCase):

    def setUp(self):
        self.integer_set = IntegerSet([1, 2, 3, 4, 5])

    def test_sum(self):
        self.assertEqual(self.integer_set.sum(), 15)

    def test_average(self):
        self.assertAlmostEqual(self.integer_set.average(), 3.0)

    def test_max(self):
        self.assertEqual(self.integer_set.max(), 5)

    def test_min(self):
        self.assertEqual(self.integer_set.min(), 1)


if __name__ == "__main__":
    unittest.main()
