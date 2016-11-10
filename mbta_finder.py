"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

import urllib2, json
from pprint import pprint
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    pprint(response_data)

get_json("https://maps.googleapis.com/maps/api/geocode/json?address=BabsonCollege")

import urllib2, json
from pprint import pprint
def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + place_name
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    print response_data["results"][0]["geometry"]["location"]

get_lat_long(BabsonCollege)
#{u'lat': 42.298139, u'lng': -71.26532929999999}


import urllib2, json
from pprint import pprint
def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=" + latitude + "&lon=" + longitude + "&format=json"
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    print response_data["stop"][0]["parent_station_name"]

get_nearest_station("42.3530197143555", "-71.0645904541016")
#Boylston

import urllib2, json
from pprint import pprint
def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
     url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + place_name
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    latitude = str(response_data["results"][0]["geometry"]["location"]["lat"])
    longitude = str(response_data["results"][0]["geometry"]["location"]["lng"])

    urla = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=" + latitude + "&lon=" + longitude + "&format=json"
    fa = urllib2.urlopen(urla)
    response_texta = fa.read()
    response_dataa = json.loads(response_texta)
    print response_dataa["stop"][0]["stop_name"]
    print response_dataa["stop"][0]["distance"]

find_stop_near("HarvardUniversity")
# Massachusetts Ave @ Wendell St
# 0.183475628495216
