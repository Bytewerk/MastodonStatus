#!/usr/bin/python3
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from mastodon import Mastodon
from settings import *


def get_state_text():
    try:
        json = requests.get(SPACE_API_URL).json()
        is_open = json['state']['open']
        state_text = STATE_OPEN if is_open else STATE_CLOSED

        last_change = json['state'].get('lastchange')
        if last_change is not None:
            timestamp = datetime.fromtimestamp(last_change)
            return timestamp.strftime(state_text)
        else:
            return state_text
    except:
        return STATE_UNKNOWN


mastodon = Mastodon(access_token=ACCESS_TOKEN_FILENAME, api_base_url=INSTANCE_URL)
updated_fields = []
for field in mastodon.account_verify_credentials().fields:
    if field['name'] == STATE_FIELD_NAME:
        updated_fields.append((STATE_FIELD_NAME, get_state_text()))
    else:
        soup = BeautifulSoup(field['value'], 'html.parser')
        updated_fields.append((field['name'], soup.get_text()))

mastodon.account_update_credentials(fields=updated_fields)
