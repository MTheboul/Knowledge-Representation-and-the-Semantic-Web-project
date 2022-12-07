"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib.request
import urllib.parse

api_key = "AIzaSyAaMn7L_OOrfDdGk4WpNNJF2PGYbyekoNQ"
searchtype = 'Person'
query = 'Forrest Gump'
print("Querying " + query + "\n\n")
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 20,
    'key': api_key,
    'prefix': True,
    'types':searchtype,
}
url = service_url + '?' + urllib.parse.urlencode(params)
response = json.loads(urllib.request.urlopen(url).read())
for element in response['itemListElement']: 
    descript =  element['result'].keys()
    if('description' in descript):
        if('actor' in str(element['result']['description']) or 'actress' in str(element['result']['description'])):
            print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')
