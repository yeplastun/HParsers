# -*- coding: utf-8 -*-

from requests import get
from json import dumps

access_token = '19212580.1677ed0.6f908ddb35564fac80cd1927abc7084e'


def getInstFollowers(artist):
    url = 'https://api.instagram.com/v1/users/'
    params = {'access_token': access_token, 'q': artist, 'count': 5}
    req = get(url + 'search', params)
    req = req.json()['data']
    res = []
    for user in req:
        r = get(url + user['id'], {'access_token': access_token})
        r = r.json()
        res.append(r['data']['counts']['followed_by'])
    if len(res) is 0:
        return 'No matching users'
    else:
        return max(res)

print(getInstFollowers('Земфира'))
