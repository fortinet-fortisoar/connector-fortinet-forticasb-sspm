"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, ACTIVITIES_API_ENDPOINT
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_user_activities(config, params):
    try:
        query = {
            "limit": params.get('limit'),
            "activity_types": params.get('activityTypes'),
            "application_names": params.get('applicationNames'),
            "user_emails": params.get('userEMails'),
            "field_time": params.get('timeSortField'),
            "start_date": params.get('startDateTime'),
            "end_date": params.get('endDateTime'),
            "order": params.get('order'),
        }
        response = api_query_call(config, query=query, endpoint=ACTIVITIES_API_ENDPOINT)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)