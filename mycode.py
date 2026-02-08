import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}


df = pd.DataFrame(data)

new_row_loc = {'Name': 'GF1', 'Age': 28, 'City': 'San Francisco' }
df.loc[len(df.index)] = new_row_loc

new_row_loc_2 = {'Name': 'GF2', 'Age': 30, 'City': 'city1' }
df.loc[len(df.index)] = new_row_loc_2

data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_date.csv')

df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")

