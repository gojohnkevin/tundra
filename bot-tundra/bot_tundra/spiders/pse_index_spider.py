import scrapy, json
from datetime import datetime

from annoying.functions import get_object_or_None
from scrapy.selector import HtmlXPathSelector

from bot_tundra.items import IndexItem
from tundra.apps.pse.models import Sector, Index

class PSEIndexSpider(scrapy.Spider):
    name = "pseindexspider"
    allowed_domains = ["www.pse.com.ph"]

    def start_requests(self):
        return [scrapy.Request("http://www.pse.com.ph/stockMarket/dailySummary.html?method=getMarketIndices", callback=self.response_data)]

    def response_data(self, response):
        res_data = json.loads(response.css('body > p::text').extract_first())
        indices = res_data.get('records', list())
        for index in indices:
            print index
