from django.conf.urls import patterns, include, url

from rest_framework import routers
from api.views import (
    SectorViewSet,
    IndexViewSet
)

router = routers.DefaultRouter()
router.register(r'sectors', SectorViewSet)
router.register(r'indices', IndexViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
