#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import tweepy

from tokens import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKE_SEARCH
from rss import get_new_items
from photos import get_random_photo


def setup_api():
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKE_SEARCH)
  return tweepy.API(auth)


api = setup_api()

new_items = get_new_items()
if new_items != []:
    for item in new_items:
        api.update_status(item)
else:
    status = get_random_photo()
    api.update_with_media('photo.jpg', status=status)
