# Botsociety Python Client

Connects to the botsociety API and provides an easy to use python API

This implementation is inspired by the official
[client for nodejs](https://github.com/botsociety/node-client).

## Installation
```
pip install -e .
```

## Usage example

```python
from botsociety import BotSocietyClient

client = BotSocietyClient(user_id="USER_ID",
                          api_key="API_KEY")
```

You can find the values for the `USER_ID` and the `API_KEY` on your [Botsociety Profile page](https://app.botsociety.io/#/account)

### auth()
Test the authentication with Botsociety.

```python
client.auth()
```
Example:
```python
In [4]: client.auth()
Out[4]:
{'auth': True,
 'info': 'You are successfully calling the API. This is just a test API to check your authentication params.'}
```

### conversations()
Retrieve all the conversations from the account.

```python
client.conversations()
```
Example:
```python
In [5]: client.conversations()
Out[5]:
[{'_id': '5af2c33e64aefa000b21b096',
  'channel': 'facebook',
  'createdAt': '2018-05-09T09:45:34.860Z',
  'name': 'testbot mockup',
  'questions': [],
  'selected_model': 'iphone6',
  'selected_variant': 'white',
  'updatedAt': '2018-05-09T12:06:51.459Z'},
 {'_id': '5af2e40964aefa000b21e108',
  'channel': 'slack',
  'createdAt': '2018-05-09T12:05:29.185Z',
  'name': 'slack-test mockup',
  'questions': [],
  'selected_model': 'iphone6',
  'selected_variant': 'white',
  'updatedAt': '2018-05-09T12:05:31.593Z'}]
```

### conversation('conversation_id')
Retrieve all the information about a single conversation (e.g. includes all messages).

```python
client.conversation("5af2c33e64aefa000b21b096")
```

Example:
```python
In [6]: client.conversation("5af2c33e64aefa000b21b096")
Out[6]:
{'_id': '5af2c33e64aefa000b21b096',
 'channel': 'facebook',
 'createdAt': '2018-05-09T09:45:34.860Z',
 'messages': [{'_belongs_to_socket_id': None,
   '_conversation': '5af2c33e64aefa000b21b096',
   '_id': '5af2c34164aefa000b21b097',
   '_sender': '5af2c34164aefa000b21b09c',
   'alternativeChoices': [],
   'attachments': [{'choices': [], 'labels': [], 'size': 'horizontal'}],
   'audio_duration': None,
   'audio_url': None,
   'audio_voice': None,
   'choices': [],
   'createdAt': '2018-05-09T09:45:37.195Z',
   'intent': 'greet',
   'is_next_message_linked': False,
   'next_alternative': None,
   'next_message': '5af2c34164aefa000b21b098',
   'prev_alternative': None,
   'prev_linked_messages': [],
   'prev_message': None,
   'progressiveId': 1,
   'show_time': 1500,
   'side': False,
   'text': 'hello',
   'text_with_variables': 'hello',
   'type': 'text',
   'updatedAt': '2018-05-09T09:49:34.469Z'}],
 'name': 'testbot mockup',
 'options': {'backgroundColor': '#FFFFFF',
  'menu': [{'id': '0f13b412-1b61-337b-4486-3278bb657443',
    'messages': [],
    'nodes': [{'id': '6308000f-8a85-a546-adc8-a6cbc96c5fb3',
      'messages': [],
      'nodes': [],
      'title': 'Contact us'}],
    'title': 'Help'}],
  'showKeyboard': True,
  'showTypingIndicators': True},
 'questions': [],
 'rtl': False,
 'selected_model': 'iphone6',
 'selected_variant': 'white',
 'set_welcome': False,
 'updatedAt': '2018-05-09T12:06:51.459Z',
 'ws_fans': '0',
 'ws_page_category': '2301',
 'ws_text': 'Hi, click the button below to start!'}
```

### message('message_id', 'conversation_id')
Retrieve all the information about a single message of a conversation.

```python
client.message("5af2c34164aefa000b21b097", "5af2c33e64aefa000b21b096")
```

Example:
```python
In [7]: client.message("5af2c34164aefa000b21b097", "5af2c33e64aefa000b21b096")
Out[7]:
{'_belongs_to_socket_id': None,
 '_conversation': '5af2c33e64aefa000b21b096',
 '_id': '5af2c34164aefa000b21b097',
 '_sender': '5af2c34164aefa000b21b09c',
 'alternativeChoices': [],
 'attachments': [{'choices': [], 'labels': [], 'size': 'horizontal'}],
 'audio_duration': None,
 'audio_url': None,
 'audio_voice': None,
 'choices': [],
 'createdAt': '2018-05-09T09:45:37.195Z',
 'intent': 'greet',
 'is_next_message_linked': False,
 'next_alternative': None,
 'next_message': '5af2c34164aefa000b21b098',
 'prev_alternative': None,
 'prev_linked_messages': [],
 'prev_message': None,
 'progressiveId': 1,
 'show_time': 1500,
 'side': False,
 'text': 'hello',
 'text_with_variables': 'hello',
 'type': 'text',
 'updatedAt': '2018-05-09T09:49:34.469Z'}
```

### variables('conversation_id')
Retrieve all variables of a conversation.

```python
client.variables("5af2c33e64aefa000b21b096")
```

Example:
```python
In [8]: client.variables("5af2c33e64aefa000b21b096")
Out[8]: {'cuisine': {'values': ['chinese']}}
```

## License
