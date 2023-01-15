import os
import logging
import json

import pandas as pd
from sqlalchemy import create_engine

user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE")

con_str = f"mysql://{user}:{password}@database/{db_name}"

# Connect to the database
engine = create_engine(con_str)

query = "SELECT country, COUNT(*) as population FROM people JOIN places ON people.place_of_birth = places.city GROUP BY country;"

output = pd.read_sql(query,engine)

# output data to json file
# output.to_json('/data/summary_output.json',orient='values')
output.set_index("country").to_json('/data/summary_output.json',orient='index')

#output data to csv file
output.to_csv('/data/summary_output.csv', sep=',', index=False)