import unittest

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def additions(self):
        return self.numbers[0] + self.numbers[1]

    def subtractions(self):
        return self.numbers[0] - self.numbers[1]

    def multiplications(self):
        return self.numbers[0] * self.numbers[1]

    def division(self):
        return self.numbers[0] / self.numbers[1]

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)

    def interest(self):
        return self.numbers[0] * self.numbers[1] * 0.01

    def degree(self):
        return self.numbers[0] ** self.numbers[1]


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator([6, 2])

    def testAdditions(self):
        self.assertEqual(self.calc.additions(), 8)

    def testSubtractions(self):
        self.assertEqual(self.calc.subtractions(), 4)

    def testMultiplication(self):
        self.assertEqual(self.calc.multiplications(), 12)

    def testDivision(self):
        self.assertEqual(self.calc.division(), 3)

    def testMax(self):
        self.assertEqual(self.calc.max(), 6)

    def testMin(self):
        self.assertEqual(self.calc.min(), 2)

    def testInterest(self):
        self.assertEqual(self.calc.interest(), 0.12)

    def testDegree(self):
        self.assertEqual(self.calc.degree(), 36)

if __name__ == '__main__':
    unittest.main()