#!/usr/bin/python3
from mastodon import Mastodon
from datetime import datetime
import requests

INSTANCE_URL = 'https://chaos.social'

try:
	json = requests.get('http://stats.bytewerk.org/status.json').json()
	state = datetime.fromtimestamp(json['state']['lastchange']).strftime('OPEN since %H:%M') if json['state']['open'] else 'closed'
except:
	state = 'unknown'

mastodon = Mastodon(access_token='usersecret.secret', api_base_url=INSTANCE_URL)
fields = [
	('Location', 'Krumenauerstr. 54 / Ingolstadt / Germany'),
	('Visit us', 'Wednesday, 19:00+ (and most other evenings)'),
	('IRC', '#bytewerk @ freenode'),
	('Status', state)
]
mastodon.account_update_credentials(fields=fields)

