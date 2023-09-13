from django.test import TestCase
from main.models import Product

'''This test checks if the attributes are using the correct data type'''
class mainTest(TestCase):
    def test_field_data_type(self):
        product = Product(name="minyak", amount=100, price=20000, description="goreng")
        
        self.assertIsInstance(product.name, str)
        self.assertIsInstance(product.amount, int)
        self.assertIsInstance(product.price, int)
        self.assertIsInstance(product.description, str)