# proquint-api
An extremely minimal API that generates pseudorandom proquints (pronounceable hash-like identifiers)

## Usage

```
curl unique.tensorturtle.com
```

## About

See https://github.com/dsw/proquint/tree/master/python for more about proquint.

## Server Setup

Ubuntu 18.04 with Caddy and Python 3.6.

## Configurations

**Systemd unit file**

Located in `/etc/systemd/system/proquint.service`

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

**Caddyfile**

Located in `/etc/caddy/Caddyfile`

```
# The Caddyfile is an easy way to configure your Caddy web server.

# static personal website
tensorturtle.com {
	reverse_proxy localhost:18080
}
# python unique proquint generator API
#
# 'http://' prefix makes Caddy to serve on http, not https.
# When served on http, 'curl unique.tensorturtle.com' works.
# if omitted, it is served on https, and 'curl https://unique.tensorturtle.com' is required.
http://unique.tensorturtle.com {
	reverse_proxy localhost:17777
}
:18080 {
	root * /home/deploy/www
	file_server
}
# Refer to the Caddy docs for more information:
# https://caddyserver.com/docs/caddyfile
```
