import os
from common.logger import setup_logger

import pandas as pd
from sqlalchemy import create_engine

logger = setup_logger("./logs/query_database.log", "DEBUG", "query_database_logger")

user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE")

con_str = f"mysql://{user}:{password}@database/{db_name}"

try:
    # Connect to the database
    engine = create_engine(con_str)
except Exception as e:
    logger.error(f"Failed to create engine: {e}")

query = "SELECT country, COUNT(*) as population FROM people JOIN places ON people.place_of_birth = places.city GROUP BY country;"

logger.info(f"query used: {query}")
output = pd.read_sql(query,engine)

# output data to json file
json_file = '/data/summary_output.json'
logger.info(f"writing data to json file: {json_file}")
output.set_index("country").to_json(json_file,orient='index')

#output data to csv file
csv_file = '/data/summary_output.csv'
logger.info(f"writing data to csv file: {csv_file}")
output.to_csv('/data/summary_output.csv', sep=',', index=False)