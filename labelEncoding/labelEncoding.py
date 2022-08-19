# To convert a variable to Label Encoding you need Label Encoder from sklearn
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('dataset.csv')

# Create Encoder Object
le = LabelEncoder()

# Apply Label Encoding
df['Modelo'] = le.fit_transform(df['Modelo'])
print(df)