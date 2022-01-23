# proquint-api

![GET API](https://github.com/tensorturtle/proquint-api/actions/workflows/get_api.yml/badge.svg)

An extremely minimal web API that generates pseudorandom proquints (pronounceable hash-like identifiers).

Some arbitrary examples: `darun-kajos`, `lakoh-rohir`, `tuvav-furim`

But actually, I made this while [yak shaving](https://en.wiktionary.org/wiki/yak_shaving).

Recreational use only. Don't use for anything of any seriousness.

If you're curious, [read the paper](https://arxiv.org/html/0901.4016) or [see the python implementation used here](https://github.com/dsw/proquint/tree/master/python)

## Usage

```
curl unique.tensorturtle.com
```

## Server Setup

Starting with Ubuntu 18.04. Example username: 'angela'

Install Caddy server: https://caddyserver.com/docs/install

Replace the Caddyfile in `/etc/caddy/Caddyfile` with:
```
# static personal website
tensorturtle.com {
        reverse_proxy localhost:18080
}
# python unique proquint generator API
#

# http backwards compatibility for curl
# 'curl unique.tensorturtle.com'
http://unique.tensorturtle.com {
        reverse_proxy localhost:17777
}
# https for browsers
https://unique.tensorturtle.com {
        reverse_proxy localhost:17777
}
:18080 {
        root * /home/deploy/www
        file_server
}
# Refer to the Caddy docs for more information:
# https://caddyserver.com/docs/caddyfile
```

From home directory, clone this repo

```bash
git clone https://github.com/tensorturtle/proquint-api.git
```

Install pip and this repo's required packages.

```bash
sudo apt install python3-pip
python3 -m pip install -r requirements.txt
```

Upload website `index.html` to `~/www`.

The home directory would look something like this:

```
/home/angela
├── proquint-api
│   ├── app.py
│   └── requirements.txt
└── www
    └── index.html
```

In the `/etc/systemd/system` directory, create a file named `proquint.service` containing:

```
[Unit]
Description=Python Flask server for proquint
After=multi-user.target

[Service]
Type=simple
User=angela
Restart=always
ExecStart=/usr/bin/python3 /home/angela/proquint-api/app.py

[Install]
WantedBy=multi-user.target
```

Start systemd service:
```bash
sudo systemctl reload-daemons
sudo systemctl enable proquint.service
sudo systemctl start proquint.service
```

## Testing

Locally:
```
pytest -s
```

Github actions tests this API at 00:00 daily (and on git push). See badge above.

## Coming soon(ish)

+ POST 
+ Traffic monitoring
