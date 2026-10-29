"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, RISK_API_ENDPOINT
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_risks(config, params):
    try:
        query = {
            "limit": params.get('limit'),
            "order": params.get('sort'),
            "min_score": params.get('minimumScore'),
            "max_score": params.get('maximumScore'),
            "sort_field": params.get('sortField')
        }
        response = api_query_call(config, query=query, endpoint=RISK_API_ENDPOINT)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)