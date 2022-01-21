# proquint-api
An extremely minimal API that generates pseudorandom proquints (pronounceable hash-like identifiers)

See https://github.com/dsw/proquint/tree/master/python for more about proquint.

Systemd unit file:
```
[Unit]
Description=Python Flask server for proquint
After=multi-user.target

[Service]
Type=simple
User=deploy
Restart=always
ExecStart=/usr/bin/python3 /home/deploy/proquint-api/app.py

[Install]
WantedBy=multi-user.target
```
