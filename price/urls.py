from rest_framework import routers
from django.conf.urls import url

from .views import PriceViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'price', PriceViewSet)

urlpatterns = router.urls