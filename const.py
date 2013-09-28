#!/usr/bin/env python

APP_KEY = '2559037599'
APP_SECRET = 'a8b8bc4af53d6272a6aee4b93fc4c715'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

OAUTH2_PARAMETER = {'client_id': APP_KEY,
                    'response_type': 'code',
                    'redirect_uri': CALLBACK_URL,
                    'action': 'submit',
                    'userId': '',  # username
                    'passwd': '',  # password
                    'isLoginSina': 0,
                    'from': '',
                    'regCallback': '',
                    'state': '',
                    'ticket': '',
                    'withOfficalFlag': 0}

