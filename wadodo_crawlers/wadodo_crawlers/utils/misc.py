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

__all__ = [
    'replace_nbrs'
]


def replace_nbrs(string):
    """
    Replace non breaking space HTML entities with actual whitespace.
    """
    return string.replace(u'\xa0', u' ')


class JoinAddress(object):
    def __init__(self):
        pass

    def __call__(self, values):
        """
        Join address in the following format:
        ['Address', 'City', 'State', 'Zip Code']
        """
        length = len(values)

        if length <= 3:
            # No zip code
            return ', '.join(values)
        elif length == 4:
            # ZIP code included
            return ', '.join(values[:3]) + ' ' + values[3]
        else:
            # TODO
            return None
