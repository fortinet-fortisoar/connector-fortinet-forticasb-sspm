"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, AUDIT_API_ENDPOINT
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_audit_log(config, params):
    try:
        query = {
            "limit": params.get('limit'),
            "sort": params.get('sort'),
            "start_date": params.get('startDate'),
            "end_date": params.get('endDate')
        }
        response = api_query_call(config, query=query, endpoint=AUDIT_API_ENDPOINT)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)