from django.conf.urls import url, include

from rest_framework import serializers

from pse.models import Sector, Index


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('name',)


class IndexSerializer(serializers.ModelSerializer):
    sector = serializers.StringRelatedField(many=False)

    class Meta:
        model = Index
        fields = ('sector', 'value', 'change', 'percent_change', 'status', 'created_at',)

