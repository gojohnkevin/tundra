from django.conf.urls import url, include

from rest_framework import serializers

from pse.models import Sector, Index


class IndexSerializer(serializers.ModelSerializer):
    value   = serializers.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Index
        fields = ('value', 'change', 'percent_change', 'status', 'created_at',)



class SectorSerializer(serializers.ModelSerializer):
    sector  = serializers.CharField(source='name')
    indices = IndexSerializer(many=True, source='index_set')

    class Meta:
        model = Sector
        fields = ('sector', 'indices',)
