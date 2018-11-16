import unittest

from calculator import calculate

class TestCalcurator(unittest.TestCase):
	def test_dodawanie(self):
		r = calculate(1, 2, '+')
		self.assertEqual(r, 3)

from calculator import str_calculator

class testStringCalculator(unittest.TestCase):
	def test_concat(self):
		r = str_calculator("a", "b", 'concat')
		self.assertEqual(r, 'ab')
