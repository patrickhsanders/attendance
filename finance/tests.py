from django.test import TestCase

from .views import get_month_from_offset
# Create your tests here.

class MonthTestCase(TestCase):
    def setUp(self):
        pass

    def test_september_minus_six(self):
        """Six months before September should be March"""
        month, year = get_month_from_offset(9, 2000, -6)
        self.assertEqual(month,3)
        self.assertEqual(year,2000)

    def test_september_plus_six(self):
        """Six months after September should be March of the following year"""
        month, year = get_month_from_offset(9, 2000, 6)
        self.assertEqual(month,3)
        self.assertEqual(year,2001)

    def test_march_minus_six(self):
        """Six months before March should be September of the previous year"""
        month, year = get_month_from_offset(3, 2000, -6)
        self.assertEqual(month, 9)
        self.assertEqual(year, 1999)

    def test_march_plus_six(self):
        """Six months after March should be September the same year"""
        month, year = get_month_from_offset(3, 2000, 6)
        self.assertEqual(month, 9)
        self.assertEqual(year, 2000)

    def test_march_plus_zero(self):
        """A month plus zero should return the same month and year"""
        month, year = get_month_from_offset(3, 2000, 0)
        self.assertEqual(month, 3)
        self.assertEqual(year, 2000)