"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, FILES_API_ENDPOINT
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_files(config, params):
    try:
        query = {
            "limit": params.get('limit'),
            "sort": params.get('sort'),
            "from_record_created_date": params.get('createDateTimeFrom'),
            "to_record_created_date": params.get('createDateTimeTo'),
            "from_record_updated_date": params.get('updateDateTimeFrom'),
            "to_record_updated_date": params.get('updateDateTimeTo')
        }
        response = api_query_call(config, query=query, endpoint=FILES_API_ENDPOINT)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)