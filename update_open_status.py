#!/usr/bin/python3
from mastodon import Mastodon
from datetime import datetime
import requests

UPDATE_FIELD_NAME = 'Status'

try:
	json = requests.get('http://stats.bytewerk.org/status.json').json()
	state = datetime.fromtimestamp(json['state']['lastchange']).strftime('OPEN since %H:%M') if json['state']['open'] else 'closed'
except:
	state = 'unknown'

mastodon = Mastodon(access_token='usersecret.secret', api_base_url='https://chaos.social')
new_fields = []
for field in mastodon.account_verify_credentials().fields:
	if field['name'] == UPDATE_FIELD_NAME:
		new_fields.append((UPDATE_FIELD_NAME, state))
	else:
		new_fields.append((field['name'], field['value']))

mastodon.account_update_credentials(fields=new_fields)

