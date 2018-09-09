from django.conf.urls import url

from .views import EnrolViewSet

url = [
    url(r'enrol', EnrolViewSet.as_view()),
]

urlpatterns = url