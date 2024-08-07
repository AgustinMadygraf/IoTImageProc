# src/services/data_extractor.py

import requests
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class DataExtractor:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch data from {self.url}: {e}")
            return None
