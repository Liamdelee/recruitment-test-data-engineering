from common.logger import setup_logger
from common.database_connection import database_connection
import json

import pandas as pd

logger = setup_logger("./logs/logs.log", "DEBUG", "query_database_logger")

database = database_connection()

query = "SELECT country, COUNT(*) as population FROM people JOIN places ON people.place_of_birth = places.city GROUP BY country;"

logger.info(f"query used: {query}")
output = pd.read_sql(query,database)

def write_to_json(data):
    json_file = '/data/summary_output.json'
    logger.info(f"Writing data to json file: {json_file}")
    ## basic writing to json file
    #data.to_json(json_file, orient='columns')
    json_data = json.loads(data.set_index("country").to_json(orient='index'))
    new_json = {key: value["population"] for key, value in json_data.items()}
    with open(json_file, "w") as outfile:
        json.dump(new_json, outfile)
    logger.info(f"Data written to json file: {json_file}")

def write_to_csv(data):
    csv_file = '/data/summary_output.csv'
    logger.info(f"writing data to csv file: {csv_file}")
    data.to_csv('/data/summary_output.csv', sep=',', index=False)
    logger.info(f"Data written to csv file: {csv_file}")

write_to_json(output)
write_to_csv(output)