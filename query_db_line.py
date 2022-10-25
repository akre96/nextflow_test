import pandas as pd
import psycopg2
from dotenv import load_dotenv
import sys, os

if os.environ.get("DB_NAME") is None:
    # Stores database credentials in to environment variables
    load_dotenv('.env')


def connect_db(study) -> psycopg2.connect:
    """ Connect to database using psycopg2

    Returns:
        psycopg2.connect: connection object
    """
    if study not in ['phase1', 'pilot']:
        raise ValueError('Study must be set to phase 1 or pilot')

    host = os.environ.get('DB_HOST')
    dbname = os.environ.get('DB_NAME')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    port = os.environ.get('DB_PORT')

    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port,
        options="-c search_path="+study,
        sslmode="require"
    )
    return conn


if __name__ == '__main__':
    conn = connect_db(sys.argv[1])
    data = pd.read_sql(
        """
        SELECT * FROM demographics
        LIMIT 1
        """,
        conn
    )
    conn.close()
    print(data)