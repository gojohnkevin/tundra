import datetime
from rest_framework import views, viewsets, filters, status
from rest_framework.response import Response

from api.serializers import SectorSerializer, IndexSerializer
from pse.models import Sector, Index

import django_filters

class SectorIndexFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(
        name='index__created_at', 
        lookup_type='gte'
    )

    class Meta:
        model = Sector
        fields = ('name', 'created')



class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all().order_by('created_at')
    serializer_class = SectorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SectorIndexFilter
    filter_fields = ('name', 'created',)


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all().order_by('-created_at')
    serializer_class = IndexSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('created_at',)


class PSEIndicesView(views.APIView):
    def get(self, request, format=None, filtering=False):
        """
        Return PSE indices
        """
        range_value = request.GET.get('range')
        yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        today = datetime.date.today()

        if range_value and range_value in ['today', 'week', 'month',]:
            filtering = True
            print 'lol'

        result = list()
        sectors = Sector.objects.all().order_by('created_at')

        for sector in sectors:
            sector_data = {
                "sector": sector.name, 
                "indices": []
            }
            if not filtering:
                context = sector.index_set.all()
            else:
                if range_value == 'today':
                    context = sector.index_set.filter(created_at__date__range=[today, today])
                    if not context:
                        context = sector.index_set.filter(created_at__date__range=[yesterday, yesterday])
            for index in context:
                index_data = {
                    "value": str(index.value),
                    "change": index.change,
                    "percent_change": index.percent_change,
                    "status": index.status,
                    "created_at": index.created_at.strftime("%Y%m%d%H%M")
                }
                sector_data['indices'].append(index_data)
            result.append(sector_data)
        return Response(result)
