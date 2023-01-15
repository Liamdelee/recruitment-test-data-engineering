from common.logger import setup_logger
from common.database_connection import database_connection
import os
import pandas as pd

logger = setup_logger("./logs/logs.log", "DEBUG", "upload_csv_database")

DATA_FILES = os.environ.get("DATA_FILES").split(',')

database = database_connection()

for data_files in DATA_FILES:

    # Read the CSV file into a pandas DataFrame
    csv_file = f'/data/input/{data_files}.csv'
    logger.info(f"Reading from: {csv_file}")
    df = pd.read_csv(csv_file)

    # Write the DataFrame data to the MYSQL database
    logger.info(f"inserting data into: {data_files}")
    df.to_sql(data_files, database, if_exists='append', index=False)