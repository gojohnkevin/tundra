from rest_framework import viewsets, filters

from api.serializers import SectorSerializer, IndexSerializer
from pse.models import Sector, Index


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all().order_by('created_at')
    serializer_class = SectorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all().order_by('-created_at')
    serializer_class = IndexSerializer
