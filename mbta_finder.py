"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def get_json(url):
    f=urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data



def get_lat_long(place_name):
    pn = place_name.split()
    ppn = str()
    for word in pn:
        ppn +=word + "+"

    pppn = ppn[:-1]
    url = GMAPS_BASE_URL + "?address=" + pppn
    result = get_json(url)
    lat = result["results"][0]["geometry"]["location"]["lat"]
    lon = result["results"][0]["geometry"]["location"]["lng"]
    re = [lat,lon]
    return re

def get_nearest_station(latitude, longitude):
    url = MBTA_BASE_URL + "?api_key=" + MBTA_DEMO_API_KEY + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&format=json"
    result = get_json(url)
    xx=99999.0
    y=str()
    for key in result[u'stop']:
        if float(key[u'distance']) < xx:
            xx = key[u'distance']
            y = key[u'stop_name']
    re = (xx,y)
    return re



def find_stop_near(place_name):
    latlon = get_lat_long(place_name)
    stadis = get_nearest_station(latlon[0],latlon[1])
    print stadis[1]
    print stadis[0]


# A little bit of scaffolding if you want to use it

find_stop_near("02481")
