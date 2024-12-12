from etl.extract import extract
import pandas as pd
from datetime import datetime
from config.bootstrap import config_logging
import logging

logger = logging.getLogger(__name__)

def transform(data):
    try:
        logger.info('Starting transformation...')

        if not data:
            logger.error("No data available to transforme")
            return None

        # Convert JSON to Dataframe
        df = pd.DataFrame(data)
        logger.info(f"Dataframe initial shape: {df.shape}")
        
        # Add timestamp column for tracking
        df['timestamp'] = datetime.now()
        logger.info(f"Dataframe updated shape: {df.shape}")

        logger.info("Data transformed successfully")
        print(df)
        return df
    
    except Exception as e:
        logger.error(f"Transformation was unsuccessful: {e}")
        raise


if __name__ == '__main__':
    config_logging()
    data = extract()
    transform(data)
