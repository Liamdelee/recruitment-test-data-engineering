from common.logger import setup_logger
from common.database_connection import database_connection
import json
import pandas as pd

class QueryDatasets:

    logger = setup_logger("./logs/logs.log", "DEBUG", "query_database_logger")

    def query_datasets(self):

        database = database_connection()
        query = "SELECT country, COUNT(*) as population FROM people JOIN places ON people.place_of_birth = places.city GROUP BY country;"

        self.logger.info(f"query used: {query}")
        output = pd.read_sql(query,database)

        json_file = '/data/summary_output.json'
        csv_file = '/data/summary_output.csv'

        self.write_to_json(output, json_file)
        self.write_to_csv(output, csv_file)

    def write_to_json(self, data, file_name):
        self.logger.info(f"Writing data to json file: {file_name}")
        ## basic writing to json file
        #data.to_json(json_file, orient='columns')
        json_data = json.loads(data.set_index("country").to_json(orient='index'))
        new_json = {key: value["population"] for key, value in json_data.items()}
        with open(file_name, "w") as outfile:
            json.dump(new_json, outfile)
        self.logger.info(f"Data written to json file: {file_name}")

    def write_to_csv(self, data, file_name):
        self.logger.info(f"writing data to csv file: {file_name}")
        data.to_csv(file_name, sep=',', index=False)
        self.logger.info(f"Data written to csv file: {file_name}")

if __name__ == "__main__":
    expr = QueryDatasets()
    expr.query_datasets()