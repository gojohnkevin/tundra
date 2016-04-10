import json, urllib
from django.utils import timezone

from django.core.management.base import BaseCommand, CommandError

from annoying.functions import get_object_or_None

from pse.models import Sector, Index

class Command(BaseCommand):
    help = 'Get current PSE Indices from each sector'

    def handle(self, *args, **options):
        url = "http://www.pse.com.ph/stockMarket/dailySummary.html?method=getMarketIndices"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        indices = data.get('records', list())
        for index in indices:
            if index.get('marketStatus') != 'CLOSED':
                sector = get_object_or_None(Sector, name=index.get('indexName'))

                if sector:
                    Index.objects.create(sector=sector, value=index.get('indexPoints'), 
                                            change=index.get('changeValue'), percent_change=index.get('percentageChange'),
                                            status=index.get('marketStatus'), created_at=timezone.now())
                    self.stdout.write(self.style.SUCCESS('Succesfully pulled data for %s.' % (sector,)))
