import json
import urllib.request
import urllib.parse

def getMostLiklySearchTerm(term, type):
    api_key = "AIzaSyAaMn7L_OOrfDdGk4WpNNJF2PGYbyekoNQ"
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': term,
        'limit': 20,
        'key': api_key,
        'prefix': True,
        'types':type,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    if(response['itemListElement'] != []):
        return response['itemListElement'][0]['result']['name']
    else:
        return "Bad Search Term"
