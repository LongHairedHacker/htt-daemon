#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from rss import get_new_items
from photos import get_random_photo

new_items = get_new_items()
if new_items != []:
    print new_items
else:
    print get_random_photo()
