from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MerchantViewSet, ProductViewSet, CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'merchants', MerchantViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart_items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
