import requests
import pandas as pd
# from config.logging_config import config_logging
import logging

def config_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

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
