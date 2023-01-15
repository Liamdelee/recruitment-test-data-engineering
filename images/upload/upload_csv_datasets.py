import os

import pandas as pd
from sqlalchemy import create_engine

DATA_FILES = os.environ.get("DATA_FILES").split(',')

user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE")

con_str = "mysql://codetest:swordfish@database/codetest"

# Connect to the database
engine = create_engine(con_str)

for data_files in DATA_FILES:

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(f'/data/input/{data_files}.csv')

    # Write the DataFrame data to the MYSQL database
    df.to_sql(data_files, engine, if_exists='append', index=False)