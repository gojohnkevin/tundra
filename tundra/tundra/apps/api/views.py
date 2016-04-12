from rest_framework import viewsets, filters

from api.serializers import SectorSerializer, IndexSerializer
from pse.models import Sector, Index

import django_filters

class SectorIndexFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(
        name='index__created_at',
    )

    class Meta:
        model = Sector
        fields = ('name', 'created')



class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all().order_by('created_at')
    serializer_class = SectorSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SectorIndexFilter
    filter_fields = ('name', 'created',)


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all().order_by('-created_at')
    serializer_class = IndexSerializer
