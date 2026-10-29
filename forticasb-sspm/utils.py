"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
from .constants import REQUEST_TIMEOUT, LOGGER_NAME, AUTH_API_ENDPOINT
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger(LOGGER_NAME)


def get_auth_token(config, **kwargs):
    try:
        url = config.get("uRL") + AUTH_API_ENDPOINT
        credentials = {
            "user_id": f"{config.get('userID')}",
            "api_key": f"{config.get('integrationKey')}"
        }
        response = requests.post(url=url, json=credentials, timeout=REQUEST_TIMEOUT)
        if not response.ok:
            logger.error("Error: {0}".format(response.content))
            raise ConnectorError('Error: {0}'.format(response.content))
        access_token = response.json()["content"]["access_token"]
        if not access_token:
            logger.error("Error: {0}".format(response.json().get("message")))
            raise Exception('Error: {0}'.format(response.json().get("message")))
        return access_token
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))


def api_query_call(config, query=None, endpoint=None, **kwargs):
    try:
        url = config.get("uRL") + endpoint
        access_token = get_auth_token(config)
        header = {'Authorization': 'Bearer ' + access_token}
        result = requests.get(url=url, params=query, headers=header, timeout=REQUEST_TIMEOUT)
        return result
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
