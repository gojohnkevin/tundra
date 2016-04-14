from django.conf.urls import patterns, include, url

from rest_framework import routers
from api.views import (
    SectorViewSet,
    IndexViewSet,
    PSEIndicesView,
)

router = routers.DefaultRouter()
router.register(r'sectors', SectorViewSet)
router.register(r'indices', IndexViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^pse-indices/$', PSEIndicesView.as_view()),
]
