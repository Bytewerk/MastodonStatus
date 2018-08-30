# update mastadon profile field with spaceapi state

this script tries to fetch a spaceapi (http://spaceapi.net/) JSON file,
parses the current space state (open / closed, since when) and updates
a mastadon profile custom field to reflect this state.

## install
```
# git clone https://github.com/Bytewerk/MastodonStatus.git
# cd MastodonStatus
# python3 -m venv venv
# venv/bin/activate
# pip install -r requirements.txt
# cp settings.py.template settings.py
```

## update config in settings.py
- set INSTANCE_URL to the base URL of your mastadon instance, e.g. 'https://chaos.social'
- set SPACE_API_URL to the URL of your spaceapi json file
- set STATE_FIELD_NAME to the name of the profile field whose value should be overwritten by this script
  you have to create this field by yourself, e.g. via your instance's website
- set STATE_[OPEN|CLOSED|UNKNOWN] texts as you like

## generate access token
the script needs a mastadon API token to operate.
you can e.g. generate that from a python REPL:
```
# python3
>>> from settings import *
>>> Mastodon.create_app('myhackerspace_open_status', api_base_url=INSTANCE_URL, to_file=CLIENT_ID_FILENAME)
>>> mastodon = Mastodon(client_id=CLIENT_ID_FILENAME, api_base_url=INSTANCE_URL)
>>> mastodon.log_in('email@example.com', 'incrediblygoodpassword', to_file=ACCESS_TOKEN_FILENAME)
```

## profit!
run the script once to check that it works, then let it run periodically, e.g. from cron.