# -*- coding: utf-8 -*-

import soundcloud
from json import dumps


def getSoundCloudFollowers(artist):
    client = soundcloud.Client(
        client_id='3661907951117885712f7ea01c76961a',
        client_secret='da6d3e8c7f8e82fc53ffb1ff336a4e24',
        username='yeplastun@gmail.com',
        password='gettherefast'
    )
    users = client.get('/search/people', q=artist)
    users = users.fields()['collection']
    res = []
    for user in users:
        res.append(int(user['followers_count']))
    if len(res) is 0:
        return 'No matching users'
    else:
        return max(res)
