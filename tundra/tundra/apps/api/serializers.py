from django.conf.urls import url, include

from rest_framework import serializers

from pse.models import Sector, Index


class IndexSerializer(serializers.ModelSerializer):
    sector = serializers.StringRelatedField(many=False)

    class Meta:
        model = Index
        fields = ('sector', 'value', 'change', 'percent_change', 'status', 'created_at',)



class SectorSerializer(serializers.ModelSerializer):
    sector  = serializers.CharField(source='name')
    indices = IndexSerializer(many=True, source='index_set')

    class Meta:
        model = Sector
        fields = ('sector', 'indices',)
