#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
from urllib import quote

import requests

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from StringIO import StringIO

YEAR = "2017"
GALLERY_URL = "http://htt-phototeam.de/gallery.json"

INPUT_RES = 1440
FONT_SIZE = 20
TEXT_COLOR = (0, 0, 0)

def make_url(year, category, photographer, pid):
    year = quote(year)
    category = quote(category)
    photographer = quote(photographer)
    pid = pid + 1
    return u"http://htt-phototeam.de/#&gid=%s/%s/%s&pid=%d" % (year, category, photographer, pid)

def pick_random_key(stuff):
    keys = stuff.keys()
    random.shuffle(keys)
    return keys[0]

def get_random_photo():
    random.seed()

    resp = requests.get(GALLERY_URL)
    json = resp.json()

    year = YEAR
    photographer = pick_random_key(json['photos'][year])
    category = pick_random_key(json['photos'][year][photographer])

    photos = json['photos'][year][photographer][category]
    pid = random.randint(0, len(photos) - 1)
    photo_url = photos[pid]['images'][unicode(INPUT_RES)]['src']

    resp = requests.get("http://htt-phototeam.de/" + photo_url)
    img = Image.open(StringIO(resp.content))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font/SourceSansPro-Regular.ttf", FONT_SIZE)
    height = img.size[1]
    draw.text((10, height - 10 - FONT_SIZE),
                "htt-phototeam.de - Photo by %s %s" % (photographer, year),
                TEXT_COLOR,
                font=font)
    img.save('photo.jpg', quality=90)

    return u"Photo des Tages: %s (%s %s)" % (make_url(year, category, photographer, pid), photographer, year)
