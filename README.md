# monkey-port
> Twilio Text Poll


### Install
----

1. Install dependencies using: `npm install`

2. Copy dependencies into the static directory (Angular, Bootstrap, etc.): `grunt copy` (may be claned using `grunt clean`)

3. Python requirements using: `pip install -r requirements.txt`

4. Rename `config_demo.py` to `config.py` and include any API keys as necessary...


### Usage
----

Twilio messaging should be set to: `/messages/incoming` (HTTP POST)