# -*- coding: utf-8 -*-

import tweepy
import re
from requests import get
from bs4 import BeautifulSoup

consumer_key = 'j3b9mAdzvH5fkfKL3XmBf7stG'
consumer_secret = '3KqL0btTbDdH4ul6Zrw2w7cVhXU7gFUf9owej68FdheIo8LTYQ'
access_token = '268859685-Uze6HQoAL4bixpBuSusRpwV0sSZtkOmOwioUdxVs'
access_token_secret = 'WziSnWtGvyaLT1TemBDeychvqNUzUBzjnIhe1T6pRtab9'


def getTweeterFollowers(artist):
    regex = '[0-9]+'
    pattern = re.compile(regex)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    users = api.search_users(artist, 5, 1)
    res = []
    for user in users:
        url = 'https://www.twitter.com/' + user.screen_name
        doc = get(url).text
        soup = BeautifulSoup(doc, 'html.parser')
        data = soup.find(
            'li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
        if data is None:
            continue
        line = str(data.a['title'])
        line = line.replace(' ', '')  # ??????
        line = line.replace(chr(160), '')
        if pattern.match(line):
            res.append(int(pattern.match(line).group()))
    if len(res) == 0:
        return 'No matching users'
    else:
        return max(res)
