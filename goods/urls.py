from rest_framework import routers
from django.conf.urls import url

from .views import OrderViewSet
from .views import GoodViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'goods', GoodViewSet)

# URLs настраиваются автоматически роутером

url = [
    url(r'orders', OrderViewSet.as_view()),
]

urlpatterns = router.urls + url