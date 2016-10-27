"""
Geocoding and Web APIs Project Toolbox
Anderson Ang Wei Jian - Toolbox #3

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json # JSon library
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def get_json(url):
    """
    Given a properly format ted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    # append URL to Google Maps API base url
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    param = urllib.urlencode(place_name)
    url = GMAPS_BASE_URL + ("?%s" % param)
    # runs json query, and stores response data
    response_data = get_json(url)
    # acquires latitude, and longtitude of location in dict respectively
    lat = response_data["results"][0]["geometry"]["location"]["lat"]
    lng = response_data["results"][0]["geometry"]["location"]["lng"]
    # enrolls the data into a tuple and returns it
    tup_loc = (lat,lng)
    return tup_loc


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    station_name = ""
    distance = 0.0
    mbta_url = MBTA_BASE_URL + "?api_key=%s&lat=%s&lon=%s&format=json" % (MBTA_DEMO_API_KEY, latitude, longitude)
    station_data = get_json(mbta_url)

    # note: exceptions do exist for having no closest stops
    # try attempts to find the closest stops
    try:
        station_name = station_data['stop'][0]['stop_name']
        distance = station_data['stop'][0]['distance']
    except:
        # exception triggered - no stops found
        print "ERROR!"

    return (station_name, distance)



def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    print "You hav entered:" + place_name + "\n"
    tuple_loc = get_lat_long({'address' : ('%s' % place_name)})
    tuple_station = get_nearest_station(tuple_loc[0],tuple_loc[1])
    print "The nearest station to this location is at " + str(tuple_station[0]) + "\n"
    print "Distance from location: " + str(tuple_station[1]) + " miles"


if __name__  == '__main__':
    find_stop_near("Yawkey Way")
    find_stop_near("Cambridge")
