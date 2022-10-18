import pandas as pd


def func_pandas():
    data = pd.read_csv('pandas_tutorial_read.csv', delimiter=';',
                       names=['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])
    print(data)

