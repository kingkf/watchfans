#!/usr/bin/env python
#-*- coding: utf-8 -*-

import const
from weibo import APIClient
    
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
uid = client.get.account__get_uid()
uid = uid['uid']
fans = client.get.friendships__followers__ids(uid=uid)
print fans
#a = u'一个傻逼应用'
#client.post.statuses__update(status=a)


            


