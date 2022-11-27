from django.urls import path, include
from rest_framework import routers

from API.views import PizzaViewSet

router = routers.DefaultRouter()
router.register(r'pizza', PizzaViewSet)
urlpatterns = [
    path(r"", include(router.urls)),
    ]
