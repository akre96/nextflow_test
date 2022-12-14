import pandas as pd
import psycopg2
from dotenv import load_dotenv
import sys, os



def connect_db(study) -> psycopg2.connect:
    """ Connect to database using psycopg2

    Returns:
        psycopg2.connect: connection object
    """
    if study not in ['phase1', 'pilot']:
        raise ValueError('Study must be set to phase 1 or pilot')

    
    if os.environ.get("DB_NAME") is None:
        raise ValueError('Set environmental variables for database connection')
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
    if os.environ.get("DB_NAME") is None:
        # Stores database credentials in to environment variables
        print('SETTING ENVIRONMENT FROM ', sys.argv[2])
        load_dotenv(sys.argv[2])
    
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