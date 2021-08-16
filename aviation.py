import requests
import json

def getMetar(icao):

    header = {'Authorization': ''}
    params = {'format': 'json', 'onfail': 'cache'}
#    r = requests.get('https://avwx.rest/api/metar/{}'.format(icao), headers=header)
    r = requests.get('https://avwx.rest/api/metar/{}?'.format(icao),params=params, headers=header)
    parsed_json = (json.loads(r.content))

    error = parsed_json.get('error')
    if error != None:
        print(error)
    else:
        print(parsed_json)
        return parsed_json.get('raw')
