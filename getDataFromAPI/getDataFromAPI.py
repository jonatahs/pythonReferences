# imports
import requests
import json
import pandas as pd


# url api with key | Add your api key here
url = 'http://ieeexploreapi.ieee.org/api/v1/search/articles?apikey=apiKey&format=json&max_records=10&start_record=1&sort_order=asc&sort_field=article_number&article_title=big+data&publication_title=big+data'

# Connecting to the api

response = requests.get(url)

# Testing api connection , if print <Response [200]>, that's mean that api it's working

print(response)

# Collecting API data

data = response.json()

print(data)
print('=====================================================================================================================================')
# Converting to Data Frame
df = pd.DataFrame(data['articles'])
print(f'O Data Frame possui: {df.shape}')
