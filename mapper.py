#!/usr/bin/env python

import json
import sys


def aboutsull(text):
    keywords = ['Theresa', 'Sullivan', 'TSully', '@terrysulli', '#Sullivan', 'Terry']
    for k in keywords:
        if k in text:
            return True
    return False


def positive(text):
     keywords = ['outrage', '#HoosforSullivan', 'support', 'great leader', 'great president', 'great President']
     for k in keywords:
         if k in text:
             return True
     return False

def anti(text):
    keywords = ['#DragasMustGo', '#SicSemperDragas']
    for k in keywords:
         if k in text:
             return True
    return False


def aboutdrag(text):
    keywords = ['Helen', 'Dragas', 'Rector', ]
    for k in keywords:
         if k in text:
             return True
    return False


with sys.stdin as f:
    for line in f:
        while True:
            try:
                data = json.loads(line)
                break
            except ValueError:
                # Not yet a complete JSON value
                line += next(f)

        # do something with the tweet

        date = data["created_at"]

        from datetime import datetime
        date_object = datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y")

        tweet_text = data["text"]

        if positive(tweet_text):
            print '{0}\t{1}'.format(date_object.timetuple().tm_yday, 1)

        line = ""
