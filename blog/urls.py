from rest_framework import routers
from django.conf.urls import url

from .views import BlogViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)

urlpatterns = router.urls