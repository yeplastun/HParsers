# -*- coding: utf-8 -*-

import re
import vk_api
import json


def getVkMembers(artist):
    login = ''
    password = ''
    vk = vk_api.VkApi(login, password)
    try:
        vk.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return 'AuthorizationError'
    params = {'q': artist, 'count': '10'}
    resp = vk.method('groups.search', params)
    resp = resp['items']
    f = open('groups.json', 'w')
    f.write(json.dumps(resp, indent=4, separators=(',', ': ')))
    regex = '^' + artist.replace(' ', ' ?-? ?')
    pattern = re.compile(regex, re.IGNORECASE)
    for group in resp:
        id = group['id']
        if pattern.match(group['name']):
            query = vk.method(
                'groups.getMembers', {'group_id': id, 'count': 0})
            res = query['count']
            return res
    return 'No matching groups'
