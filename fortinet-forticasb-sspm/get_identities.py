"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, IDENTITIES_API_ENDPOINT
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_identities(config, params):
    try:
        query = {
            "limit": params.get('limit'),
        }
        response = api_query_call(config, query=query, endpoint=IDENTITIES_API_ENDPOINT)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)