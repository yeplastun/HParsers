# -*- coding: utf-8 -*-

import tweepy
from requests_oauthlib import OAuth1Session


def getTweeterFollowers(artist):
    consumer_key = 'j3b9mAdzvH5fkfKL3XmBf7stG'
    consumer_secret = '3KqL0btTbDdH4ul6Zrw2w7cVhXU7gFUf9owej68FdheIo8LTYQ'
    access_token = '268859685-Uze6HQoAL4bixpBuSusRpwV0sSZtkOmOwioUdxVs'
    access_token_secret = 'WziSnWtGvyaLT1TemBDeychvqNUzUBzjnIhe1T6pRtab9'
    regex = '[0-9]+'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    users = api.search_users(artist, 5, 1)
    res = []
    for user in users:
        url = 'https://api.twitter.com/1.1/users/lookup.json?screen_name=' + \
            user.screen_name
        getUsr = OAuth1Session(consumer_key,
                               client_secret=consumer_secret,
                               resource_owner_key=access_token,
                               resource_owner_secret=access_token_secret)
        resp = getUsr.get(url).json()
        res.append(int(resp[0]['followers_count']))

    if len(res) == 0:
        return 'No matching users'
    else:
        return max(res)
