import unittest

from calculator import calculate

class TestCalcurator(unittest.TestCase):
	def test_dodawanie(self):
		r = calculate(1, 2, '+')
		self.assertEqual(r, 3)

	def test_odejmowanie(self):
		s = calculate(3, 2, '-')
		self.assertEqual(s,1)

	def test_mnozenie(self):
		t = calculate(2, 3, '*')
		self.assertEqual(t, 6)


from calculator import str_calculator

class testStringCalculator(unittest.TestCase):
	def test_concat(self):
		r = str_calculator("a", "b", 'concat')
		self.assertEqual(r, 'ab')
