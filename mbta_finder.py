"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json



def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
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
    placenamewords = place_name.split()
    baseurl = "https://maps.googleapis.com/maps/api/geocode/json?address="
    first = True
    #compose with %20 delimiter
    for word in placenamewords:
        if first:
            first = False
            baseurl = baseurl + word
        else:
            baseurl = baseurl + "%20" + word
    json = get_json(baseurl)
    #step thru jason to find lat and long
    lat =  json["results"][0]["geometry"]["location"]["lat"]
    lng = json["results"][0]["geometry"]["location"]["lng"]
    return [str(lat),str(lng)]

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    # the mbta api url (with key) in 3 base strings seperated by lat and lon
    mbta_baseurl = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat="
    mbta_baseurl2 = "&lon="
    mbta_baseurl3 = "&format=json"
    mbtajson = get_json(mbta_baseurl+latitude+mbta_baseurl2+longitude+mbta_baseurl3)
    closeststopname = mbtajson
    #try to index to nearest station, let user know if none exist
    try:
        distance = closeststopname['stop'][0]["distance"]
        name = closeststopname['stop'][0]["stop_name"]
    except:
        print "No nearby stations."
    return (name,distance)

    

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat_long = get_lat_long(place_name)
    nearest_station = get_nearest_station(lat_long[0],lat_long[1])
    print "Nearest station is : " + nearest_station[0] + "\n"
    print "Distance:" + nearest_station[1] + " miles"
    


find_stop_near("Massachusetts Institute of Technology")
