import requests
import pandas as pd
from config.bootstrap import config_logging #, configure_project_root
import logging

config_logging()

logger = logging.getLogger(__name__)

def extract():
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        logger.info("Starting data extraction...")

        # Get data
        response = requests.get(url)
        response.raise_for_status() ## Raise HTTPError for bad response
        data = response.json()
        df = pd.DataFrame(data)
        logger.info(f'Number of columns: {len(df.columns)} & Number of Rows {len(df.index)}')
        return df
    except requests.exceptions.RequestException as e:
        logger.info(f'Error during data extraction: {e}')
        raise


# Check data exists
df = extract()
print(df)
# python -m etl.extract, need to run as modules
