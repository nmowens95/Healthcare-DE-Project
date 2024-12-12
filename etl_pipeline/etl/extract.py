import requests
import pandas as pd
from config.bootstrap import config_logging #, configure_project_root
import logging

logger = logging.getLogger(__name__)

def extract():
    # API url
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        logger.info("Starting data extraction...")

        # Get data
        response = requests.get(url)
        response.raise_for_status() ## Raise HTTPError for bad response
        data = response.json()
        logger.info("Data extraction completed successfully")
        # print(data)
        return data
    
    except requests.exceptions.RequestException as e:
        logger.info(f'Error during data extraction: {e}')
        raise

# Check data exists
if __name__ == "__main__":
    config_logging() # Set up logging within main so it doesn't carry to other files
    extract()
# python -m etl.extract, need to run as modules
