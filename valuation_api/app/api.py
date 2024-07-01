import requests
from .config import Config
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class FinancialAPI:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.base_url = Config.BASE_URL

    def fetch_data(self, statement_type, company, years=Config.YEARS):
        try:
            url = f"{self.base_url}{statement_type}/{company}?apikey={self.api_key}&limit={years}"
            logger.debug(f"Fetching data from URL: {url}")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            logger.debug(f"Received data: {data}")
            return data
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return None


    def fetch_company_profile(self, symbol):
        try:
            url = f"{self.base_url}profile/{symbol}?apikey={self.api_key}"
            logger.debug(f"Fetching company profile from URL: {url}")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            logger.debug(f"Received company profile data: {data}")
            return data[0] if data else None
        except requests.RequestException as e:
            logger.error(f"Error fetching company profile: {e}")
            return None