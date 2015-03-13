import random_walk
import pylab
from unittest import TestCase


class TestStock(TestCase):

	def test_check_negative_stock(self, value):
		self.assertRaises(ValueError, "Stocks cannot be negative")
	def test_check_zero_stock(self, value):
		pass

	def test_check_big_stock(self, value):
		pass


class TestPrice(TestCase):

	def test_negative_price(self, value):
		pass

	def test_zero_price(self, value):
		pass

	def test_high_price(self, value): # check price ceiling
		pass

class TestBias(TestCase):

	def test_bias_range(self, value):
		pass


class TestDays(TestCase):

	def test_days_range(self, value):
		pass

class TestDataType(TestCase):
	
	def test_if_string(self, value):
		pass

	def test_if_integer(self, value):
		pass

	def test_if_float(self, value):
		pass

	def test_if_dict(self, value):
		pass

	def test_if_list(self, value):
		pass


def run_test_case():
	pass

def pass_params():
	pass