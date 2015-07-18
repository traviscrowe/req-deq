__author__ = 'traviscrowe'

import api_keys as keys
import requests, json

def run():
    city = 'appleton'#input('City: ')
    state = 'wi'#input('State: ')
    search_radius = '25'#input('Search radius: ')
    max_results = '25'#input('Max results: ')

    #still working out best query for a general dev search
    url = 'http://api.indeed.com/ads/apisearch?publisher=' + keys.INDEED
    query = '&q=developer%2C+programmer%2C+C%23&+java%2C+javascript%2C&l=' + \
            city + '%2C+' + state + '&limit='+ max_results + '&radius=' + search_radius + '&sort=date&start=25&format=json&v=2'

    page = requests.get(url + query)

    js = json.loads(page.text)

    #results = js['results']

    #for result in results:
        #print(result)
        #print(result['company'] + ' | ' + result['jobtitle'] + ' | '+ result['formattedRelativeTime'])

    print(page.text)
    print('Request URL: ' + url + query)
    print('Total Results: ' + str(js['totalResults']))


run()