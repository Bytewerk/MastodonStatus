# initial init

### install Mastodon.py
```
sudo pip3 install Mastodon.py
```

### create App credentials
```
Mastodon.create_app('bytewerk_open_status', api_base_url='https://chaos.social', to_file='clientcred.secret')
```

### log in once with password
```
mastodon = Mastodon(client_id='clientcred.secret', api_base_url='https://mastodon.social')
mastodon.log_in('email@example.com', 'incrediblygoodpassword', to_file='usersecret.secret')
```

### run update_open_status.py from cron
