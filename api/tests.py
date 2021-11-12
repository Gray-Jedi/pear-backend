from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model
from .models import *

class ApiTests(TestCase):

    def setUp(self): 
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="pass")

        self.item = Product.objects.create(
            name ="shoes", 
            brand ="nike",
            category ="clothes",
            description ="black and white size 9",
            price = 60,
        )

        self.order = Order.objects.create(
            paymentMethod = "paypal", 
            taxPrice = 1,
            totalPrice = 1,
            isPaid = True,
            isDelivered = True,
        ) 

        self.order_item = OrderItem.objects.create(
            name = "shirt",
            qty = 7,
            price = 125,
        ) 

        self.location_address = LocationAddress.objects.create(
            address = "123 Pike St",
            city = "Seattle",
            postalCode = "12567",
            country = 'United States',
        ) 

    def test_user_name_should_default_to_email_fail(self):
        self.assertNotEqual(f'{self.user}', 'testuser')

    def test_user_name_should_default_to_email_success(self):
        self.assertEqual(f'{self.user}', 'test@test.com')

    def test_timestamps(self): 
        self.assertIsInstance(self.item.createdAt, datetime)
        self.assertIsInstance(self.order.createdAt, datetime)

    def test_product_field_types(self):
        self.assertIsInstance(self.item.name, str)
        self.assertIsInstance(self.item.brand, str)
        self.assertIsInstance(self.item.category, str)
        self.assertIsInstance(self.item.description, str)
        self.assertIsInstance(self.item.price, int)

    def test_order_field_types(self): 
        self.assertIsInstance(self.order.paymentMethod, str)
        self.assertIsInstance(self.order.taxPrice, int)
        self.assertIsInstance(self.order.totalPrice, int)
        self.assertIsInstance(self.order.isPaid, bool)
        self.assertIsInstance(self.order.isDelivered, bool)

    def test_order_item_field_types(self):
        self.assertIsInstance(self.order_item.name, str)
        self.assertIsInstance(self.order_item.qty, int)
        self.assertIsInstance(self.order_item.price, int)

    def test_location_addr_field_types(self):
        self.assertIsInstance(self.location_address.address, str)
        self.assertIsInstance(self.location_address.city, str)
        self.assertIsInstance(self.location_address.postalCode, str)
        self.assertIsInstance(self.location_address.country, str)

    def test_product_repr(self):
        self.assertEqual(str(self.item.name), "shoes")
        self.assertEqual(str(self.item.brand), "nike")
        self.assertEqual(str(self.item.category), "clothes")
        self.assertEqual(str(self.item.description), "black and white size 9")
        self.assertEqual(int(self.item.price), 60)

    def test_order_repr(self):
        self.assertEqual(str(self.order.paymentMethod), "paypal")
        self.assertEqual(int(self.order.taxPrice), 1)
        self.assertEqual(int(self.order.totalPrice), 1)
        self.assertEqual(bool(self.order.isPaid), True)
        self.assertEqual(bool(self.order.isDelivered), True)

    def test_order_item_repr(self):
        self.assertEqual(str(self.order_item.name), "shirt")
        self.assertEqual(int(self.order_item.qty), 7)
        self.assertEqual(int(self.order_item.price), 125)

    def test_location_addr_repr(self):
        self.assertEqual(str(self.location_address.address), "123 Pike St")
        self.assertEqual(str(self.location_address.city), "Seattle")
        self.assertEqual(str(self.location_address.postalCode), "12567")
        self.assertEqual(str(self.location_address.country), "United States")
