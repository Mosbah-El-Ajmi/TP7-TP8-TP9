import unittest

from TP7 import Fraction

class TestFraction(unittest.TestCase):
    """This class is a test class for the Fraction class.

        Author : Mosbah El-Ajmi
        Date : December 2022
    """
    def test_init(self):
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(-3, 4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(3, -4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(-3, -4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(0, 4)
        self.assertEqual(f.numerator, 0)
        self.assertEqual(f.denominator, 1)

        with self.assertRaises(ZeroDivisionError):
            Fraction(3, 0)

        with self.assertRaises(ValueError):
            Fraction("a","b")

    def test_str(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

        f = Fraction(4, 4)
        self.assertEqual(str(f), "1")

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6))

        f1 = Fraction(1, 2)
        f2 = Fraction(2, 2)
        self.assertEqual(f1 + f2, Fraction(3, 2))

    def test_sub(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 - f2, Fraction(1, 6))

        f1 = Fraction(1, 2)
        f2 = Fraction(2, 2)
        self.assertEqual(f1 - f2, Fraction(-1, 2))

    def test_mul(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 * f2, Fraction(1, 6))

    def test_truediv(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 / f2, Fraction(3, 2))

        f1 = Fraction(1, 2)
        f2 = Fraction(2, 2)
        self.assertEqual(f1 / f2, Fraction(1, 2))

        f1 = Fraction(1, 2)
        f2 = Fraction(0, 2)
        with self.assertRaises(ZeroDivisionError):
            f1 / f2

    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 == f2)

        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertFalse(f1 == f2)

    def test_reduce(self):
        f = Fraction(2, 4)
        f.reduce()
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

    def test_as_mixed_number(self):
        f = Fraction(5, 2)
        self.assertEqual(f.as_mixed_number(), "2 1/2")

        f = Fraction(4, 4)
        self.assertEqual(f.as_mixed_number(), "1")

        f = Fraction(1, 2)
        self.assertEqual(f.as_mixed_number(), "1/2")

    def test_pow(self):
        f = Fraction(5, 2)
        f2 = Fraction(4, 4)
        value = f**f2
        self.assertEqual(value.as_mixed_number(), "2 1/2")

    def test_is_nul(self):
        f = Fraction(0,1)
        self.assertTrue(f)


if __name__ == "__main__":
    unittest.main()
