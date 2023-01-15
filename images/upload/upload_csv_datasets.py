import os
from common.logger import setup_logger

import pandas as pd
from sqlalchemy import create_engine

logger = setup_logger("./logs/upload_csv_database.log", "DEBUG", "upload_csv_database")

DATA_FILES = os.environ.get("DATA_FILES").split(',')

user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE")

con_str = f"mysql://{user}:{password}@database/{db_name}"

try:
    # Connect to the database
    engine = create_engine(con_str)
except Exception as e:
    logger.error(f"Failed to create engine: {e}")

for data_files in DATA_FILES:

    # Read the CSV file into a pandas DataFrame
    csv_file = f'/data/input/{data_files}.csv'
    logger.info(f"Reading from: {csv_file}")
    df = pd.read_csv(csv_file)

    # Write the DataFrame data to the MYSQL database
    logger.info(f"inserting data into: {data_files}")
    df.to_sql(data_files, engine, if_exists='append', index=False)