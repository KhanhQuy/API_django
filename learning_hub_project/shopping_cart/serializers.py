from rest_framework import serializers
from .models import User, Merchant, Product, Cart, CartItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'merchant']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'delivery_distance', 'items']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['total_fee'] = instance.delivery_distance / 500 * 10 + sum(item.product.price * item.quantity for item in instance.cartitem_set.all())
        return rep
