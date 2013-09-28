#!/usr/bin/env python

import const
from weibo import APIClient

def authorize(authorize_url, username, password):
    from urllib import urlencode
    import requests

    oauth2 = const.OAUTH2_PARAMETER
    oauth2['userId'] = username
    oauth2['passwd'] = password
    postdata = urlencode(oauth2)

    print authorize_url
    headers = {'Referer': authorize_url,
               'Content-Type': 'application/x-www-form-urlencode'}
    res = requests.post("https://api.weibo.com/oauth2/authorize", data=postdata, headers=headers, verify=True)
#    res = requests.post(authorize_url, data=postdata, headers=headers, verify=True)
    print res.headers
    

#username = raw_input("Username: ")
#password = raw_input("Password: ")
username = "jkflovezzy@gmail.com"
password = "j1k2f3abc"

client = APIClient(app_key=const.APP_KEY, app_secret=const.APP_SECRET,
                   redirect_uri=const.CALLBACK_URL)

authorize_url = client.get_authorize_url()
authorize(authorize_url, username, password)

            


