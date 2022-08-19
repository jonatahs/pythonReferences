import pandas as pd
# Load json to dataframe

reading = pd.read_json('arquivo.json')

#view data frame

print(reading.head())