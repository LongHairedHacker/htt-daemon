#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

import feedparser
from lxml import html

URLS_LIST = 'urls.lst'
RSS_URL = 'https://htt-spirkelbach.de/feed/'

def load_old_urls():
    urls = []

    if os.path.isfile(URLS_LIST):
        for url in open(URLS_LIST, 'r'):
            urls += [url.strip()]

    return urls


def save_old_urls(urls):
    urls_file = open(URLS_LIST, 'w')
    for url in urls:
        urls_file.write('%s\n' % url)
    urls_file.close()


def get_new_items():
    old_urls = load_old_urls()
    rss = feedparser.parse(RSS_URL)

    new_items = []

    for item in sorted(rss.entries, key=lambda x: x.published_parsed):
        url = item.link
        if not (url in old_urls):
            if len(item.description) > 0:
                text = html.fromstring(item.description).text_content()
                if len(text) > 1:
                    text = ' '.join(text.split())
                    new_items += [u'%s…\n%s' % (text[0:80], url)]
                    old_urls += [url]

    save_old_urls(old_urls)

    return new_items
