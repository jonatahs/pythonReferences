# To convert a variable to Dummie you need pandas
# Imports 
import pandas as pd
df = pd.read_csv('dataset.csv')
# Generate Dummie variables
dfDummies = pd.get_dummies(df['Modelo'])
# Concat df and dfDummies
newDf = pd.concat([df,dfDummies], axis='columns')
print(newDf)