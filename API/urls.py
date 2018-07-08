from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import ListCampaigns
from .views import ListLocations

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'campaigns', ListCampaigns)
router.register(r'locations', ListLocations)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^api/', include(router.urls))
]
