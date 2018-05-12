# Botsociety Python Client

Connects to the botsociety API and provides an easy to use python API

This implementation is inspired by the official
[client for nodejs](https://github.com/botsociety/node-client).

## Installation
```
pip install botsociety-client
```

## Usage example

```python
from botsociety import BotSocietyClient
client = BotSocietyClient(user_id="USER_ID",
                          api_key="API_KEY")
```

### auth()
Tests the authentication with Botsociety.

```python
client.auth()
```
Example:
```python
In [5]: client.auth()
Out[5]:
{u'auth': True,
 u'info': u'You are successfully calling the API. This is just a test API to check your authentication params.'}
```

## License