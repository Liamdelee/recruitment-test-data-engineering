import os
import logging
import json

import pandas as pd
from sqlalchemy import create_engine

user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE")

con_str = "mysql://codetest:swordfish@database/codetest"

# Connect to the database
engine = create_engine(con_str)

query3 = "SELECT country, COUNT(*) as population FROM people JOIN places ON people.place_of_birth = places.city GROUP BY country;"

output3 = pd.read_sql(query3,engine)
output_json = output3.to_json(orient="values")

print(output_json)