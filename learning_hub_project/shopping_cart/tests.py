from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from .models import User, Merchant, Product, Cart, CartItem

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Test User")
        self.merchant = Merchant.objects.create(name="Test Merchant")
        self.product = Product.objects.create(name="Test Product", price=50.0, merchant=self.merchant)
        self.cart = Cart.objects.create(user=self.user, delivery_distance=1000.0)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_model_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Merchant.objects.count(), 1)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(CartItem.objects.count(), 1)

class ViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name="Test User")
        self.merchant = Merchant.objects.create(name="Test Merchant")
        self.product = Product.objects.create(name="Test Product", price=50.0, merchant=self.merchant)
        self.cart = Cart.objects.create(user=self.user, delivery_distance=1000.0)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_get_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_merchants(self):
        response = self.client.get(reverse('merchant-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_carts(self):
        response = self.client.get(reverse('cart-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_get_cart_items(self):
        response = self.client.get(reverse('cartitem-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
