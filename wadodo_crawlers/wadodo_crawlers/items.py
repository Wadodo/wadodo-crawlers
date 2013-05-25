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

from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join
from scrapy.contrib.loader.processor import Identity

from wadodo_crawlers.utils.misc import replace_nbrs, JoinAddress


class ActivityItem(Item):
    name = Field()
    categories = Field()
    address = Field()
    phone_number = Field()
    website = Field()
    description = Field()
    time_needed = Field()
    price = Field()

    source_url = Field()
    image_urls = Field()
    images = Field()


class ActivityItemLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

    name_out = TakeFirst()
    categories_out = Identity()
    address_in = MapCompose(unicode.strip)
    address_out = JoinAddress()
    description_in = MapCompose(replace_nbrs)
    description_out = Join('\n')
    time_needed_out = TakeFirst()
    price_out = TakeFirst()
    image_urls_out = Identity()
    images = Identity()
