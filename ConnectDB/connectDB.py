# import sqlalchemy | create_engine function 
from sqlalchemy import create_engine
import pandas as pd

# create database connection
engine = create_engine('sqlite:///data.db')

# writing query 
query = """SELECT date,
                  tmax,
                  tmin
            FROM weather;
        """
# Making a dataframe 
df = pd.read_sql(query,engine)

print(df.head())
