import os

import pandas as pd
from query.query_datasets import QueryDatasets

def test_write_to_json():
    data_input = {'country': [1, 2], 'population': [3, 4]}
    df = pd.DataFrame(data=data_input)
    output_file = "test_write_to_json.json"
    expr = QueryDatasets()
    expr.write_to_json(df, output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)


def test_write_to_csv():
    data_input = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=data_input)
    output_file = "write_to_csv.csv"
    expr = QueryDatasets()
    expr.write_to_csv(df, output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)