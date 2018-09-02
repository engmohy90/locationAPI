from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TemperatureViewSet
# from .views import ListLocations
from .views import send_push

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tempLog', TemperatureViewSet)
# router.register(r'locations', ListLocations)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^push/', send_push),
]
