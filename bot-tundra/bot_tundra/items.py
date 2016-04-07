# -*- coding: utf-8 -*-
from scrapy_djangoitem import DjangoItem

from tundra.apps.pse.models import Index


class IndexItem(DjangoItem):
    django_model = Index
