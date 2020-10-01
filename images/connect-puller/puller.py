import json
import glob
import requests

kc_cluster = 'http://kafka-connect:8083'
connectors_pull_url = 'https://raw.githubusercontent.com/renanpolisciuc/kafka-connect-poc/master/connectors.json'

connectors = requests.get('{0}/connectors'.format(kc_cluster)).json()

print('Connectors:')
for c in connectors:
  print(c)

print('-----')

print("Downloading connectors...")
connectors_pull = requests.get(connectors_pull_url).json()
print("Connectors:")
print(connectors_pull)
for c in connectors_pull:
  try:
    print("Connector:")
    print(c)
    if not c['name'] in connectors:
      post_connector = requests.post('{0}/connectors'.format(kc_cluster), headers = {'content-type': 'application/json'}, data=json.dumps(c)).json()
      print(post_connector)
  except Exception as e:
    print(e)
    
print("Finish")

