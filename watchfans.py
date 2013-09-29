#!/usr/bin/env python
#-*- coding: utf-8 -*-

import const
import os
import cPickle
import time
from weibo import APIClient

def id_exists(uid):
    try:
        client.get.users__show(uid=uid)
    except:
        return False
    return True

client = APIClient(app_key=const.APP_KEY, app_secret=const.APP_SECRET,
                   redirect_uri=const.CALLBACK_URL)

#authorize_url = client.get_authorize_url()
#print authorize_url
#authorize_code = raw_input("code: ")
#r = client.request_access_token(authorize_code)
#
#print r.access_token
#print r.expires_in
access_token = '2.00zK_ymBzZ9LnC0901f4c7f4YXVgRE'
expires_in = '1538066743'
client.set_access_token(access_token, expires_in)
myuid = client.get.account__get_uid()['uid']
if os.path.exists(const.PERSISTENCE_FILE):
    current_fans = cPickle.load(open("data/data.pkl","rb"))
else:
    current_fans = set(client.get.friendships__followers__ids(uid=myuid)['ids'])
    cPickle.dump(current_fans, open("data/data.pkl", "wb"))

while True:
    pre_fans = current_fans
    current_fans = set(client.get.friendships__followers__ids(uid=myuid)['ids'])
    if current_fans != pre_fans:
        cPickle.dump(current_fans, open("data/data.pkl", "wb"))

    lose_fans = []
    for fan in  pre_fans:
        if fan not in current_fans:
            lose_fans.append(fan)

    lose_fans = [f for f in lose_fans if id_exists(f)]
    if lose_fans:
        lose_status = u'哼!%s干嘛取消关注我! '
        lose_fans_name = [client.get.users__show(uid=uid)['screen_name'] for uid in lose_fans]
        if len(lose_fans) == 1:
            lose_status = lose_status % u'你'
        else:
            lose_status = lose_status % u'你们'

        name_status = ['@'+name for name in lose_fans_name]
        print lose_status+''.join(name_status)
        client.post.statuses__update(status=lose_status+''.join(name_status))
    time.sleep(60)
