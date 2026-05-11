from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from django.utils.module_loading import import_string
from .builtins import *
from .constants import LOGGER_NAME, RISK_API_ENDPOINT
logger = get_logger(LOGGER_NAME)
from .utils import api_query_call


class Forticasb_sspm(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        return supported_operations.get(operation)(config, params)

    def check_health(self, config=None, *args, **kwargs):
        try:
            response = api_query_call(config, query="limit=1", endpoint=RISK_API_ENDPOINT)
            if response.ok:
                logger.info("Connector is available")
                return True
            else:
                raise ConnectorError(f"Error {response.status_code} - {response.text}")
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)