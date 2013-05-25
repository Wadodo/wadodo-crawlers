# Licensed to Tomaz Muraus under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# Tomaz muraus licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from wadodo_crawlers.items import ActivityItem, ActivityItemLoader
from wadodo_crawlers.spiders.base import FlickrCrawlSpider

LAS_VEGAS_TO_WADODO_CATEGORY_MAP = {
    'Clubs And Lounges': 'Nightlife',
    'Cultural Activity': 'Arts',
    #'Family Friendly': '',
    #'Free Attraction': ,
    'Movie Theater': 'Theatre',
    'Museums And Exhibits': ['Heritage', 'Art'],
    'Spa': ['Relaxation & Spa'],
    'Thrill Rides & Roller Coasters': ['Adrenaline'],
    'Ultimate Pools': ['Relaxation & Spa'],
}


class LasVegasDotCom(FlickrCrawlSpider):
    name = 'lasvegas.com'
    allowed_domains = ['lasvegas.com']
    start_urls = [
        'http://www.lasvegas.com/activities/attractions/?catid=55&destid=0&fieldid=0&maxshow=500&random_sort=0&regionid=4,2,3&subcatid=0'
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=('/listing/.+?/', ),
                               restrict_xpaths=['//div[@class="listingItem"]']), callback='parse_activity'),
    ]
    def __init__(self, *args, **kwargs):
        super(FlickrCrawlSpider, self).__init__(*args, **kwargs)

    def parse_activity(self, response):
        hxs = HtmlXPathSelector(response)

        l = ActivityItemLoader(item=ActivityItem(), response=response)
        l.add_xpath('name', '//h2[@class="itemTitle"]/text()')
        l.add_xpath('address', '//p[@class="listingAddress"]/text()')
        l.add_xpath('description', '//div[@class="overviewBottom"]/p/text()')

        l.add_value('source_url', response.url)

        type = hxs.select('//p[@class="lodgingtype"]/text()').extract()[0]

        item = l.load_item()
