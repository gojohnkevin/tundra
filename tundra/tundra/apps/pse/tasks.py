import json, urllib, os

from django.utils import timezone

from annoying.functions import get_object_or_None
from celery import Celery
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger

from pse.models import Sector, Index


app = Celery('tundra')
logger = get_task_logger(__name__)


@app.task(name='get_pse_sector_indices')
def get_pse_sector_indices():
    logger.info("Retrieving PSE sectors indices...")

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
                logger.info('Succesfully pulled data for %s.' % (sector,))
