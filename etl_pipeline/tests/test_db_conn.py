import pytest
import psycopg2
from psycopg2 import sql, Error
from dotenv import load_dotenv

load_dotenv()

#postgresql+psycopg2://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


# def test_conn():
    # conn = psycopg2.connect(
    # host=os.getenv(DB_HOST),
    # database=os.getenv(DB_NAME),
    # user=os.getenv(DB_USERNAME),
    # password=os.getenv(DB_PASSWORD)
    # )
    # conn.close()


def test_connection(url):
    conn = psycopg2.connect(url)

    cursor = conn.cursor()

    cursor.execute("Select version();")

    version = cursor.fetchone()
    print(f'Postgres version {version}')

    cursor.close()
    conn.close()
