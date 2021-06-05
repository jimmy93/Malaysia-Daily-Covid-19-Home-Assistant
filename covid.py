import csv
import requests
import json
url = 'https://raw.githubusercontent.com/wnarifin/covid-19-malaysia/master/covid-19_my.csv' #read csv file
resp = requests.get(url)
decoded_content = resp.content.decode('utf-8')
reader = csv.DictReader(decoded_content.splitlines(), delimiter = ',')
list_from_csv = []  #make a list
for row in reader:
    list_from_csv.append(row)
print(json.dumps(list_from_csv[-1]))  #print json format for the last row -1
