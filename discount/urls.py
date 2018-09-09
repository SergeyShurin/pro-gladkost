from rest_framework import routers
from django.conf.urls import url

from .views import DiscountViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'discount', DiscountViewSet)

urlpatterns = router.urls