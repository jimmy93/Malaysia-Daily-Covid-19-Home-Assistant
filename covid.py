import requests
import sys
import csv
import json

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
resp = requests.get(url)
decoded_content = resp.content.decode('utf-8')
reader = csv.DictReader(decoded_content.splitlines(), delimiter=',')

states = {'Pennsylvania', 'New Jersey'}
state = sys.argv[1]
county = {}
for row in reader:
    if row['state'] == state:
        county[row['county']+'_cases'] = int(row['cases'])
        county[row['county']+'_deaths'] = int(row['deaths'])    
        county['last_date'] = row['date']
        
# CSV is in sorted order, so whatever is left is the most recent.

# Calulcate state-level info
state_cases = 0
state_deaths = 0
for key, val in county.items():
    if key.endswith('deaths'):
        state_deaths += val
    elif key.endswith('cases'):
        state_cases += val

county['state_level_cases'] = state_cases
county['state_level_deaths'] = state_deaths

# This will print out the dict in json format for easy parsing in HA.
print(json.dumps(county))