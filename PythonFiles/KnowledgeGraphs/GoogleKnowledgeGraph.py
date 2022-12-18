import json
import urllib.request
import urllib.parse

# Google knowledge graf is only used for its ability to handle incomplete input
# and is used to take incomplete input and return the most likly search term in
# correct format. No use of the knowledge graf is taking place and therefor not
# in the rapport.
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
