from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import logging

import requests

logger = logging.getLogger(__name__)


class BotSocietyClient(object):
    API_URL = "https://app.botsociety.io/apisociety"

    API_VERSION = "1.1"

    def __init__(self,
                 user_id,
                 api_key):
        self.user_id = user_id
        self.api_key = api_key

    def _call_api(self, sub_url, api_version=None):
        local_api = api_version or self.API_VERSION

        url = "{}/{}/{}".format(self.API_URL,
                                local_api,
                                sub_url)

        logger.debug("Calling Botsociety API '{}'".format(url))

        headers = {
            'Content-Type': 'application/json',
            'user_id': self.user_id,
            'api_key_public': self.api_key
        }

        result = requests.get(url, headers=headers)

        result.raise_for_status()

        logger.debug("Botsociety API Response Code: {} Content: '{}'".format(
                result.status_code, result.json))

        return result.json()

    def auth(self):
        return self._call_api("")

    def conversation(self, conversation_id):
        sub_url = "conversations/{}".format(conversation_id)
        return self._call_api(sub_url)

    def conversations(self):
        return self._call_api("conversations")

    def message(self, message_id, conversation_id):
        sub_url = "conversations/{}/messages/{}".format(
                message_id, conversation_id)
        return self._call_api(sub_url)

    def variables(self, conversation_id):
        sub_url = "conversations/{}/variables".format(conversation_id)
        return self._call_api(sub_url)
