from dotenv import load_dotenv
load_dotenv()

import numpy as np
import os
import googlemaps
from models import Location
from typing import List, Optional, Tuple

gmaps = googlemaps.Client(key=os.getenv('GMAPS_KEY'))

def get_route(waypoints: List[Location], start: Location, end: Location) -> Tuple(Location):
    """Return waypoints (start location, ending location) that are closest for a specific start and end location"""
    startpts = [l for l in waypoints if l.startpt]
    endpts = [l for l in waypoints if l.endpt]
    # closest_start = [l for l in waypoints if Location.dist(l, start) == min([Location.dist(l, start) for l in startpts])]
    return closest_loc(startpts, start), closest_loc(endpts, end)
        
def closest_loc(waypoints: List[Location], loc: Location) -> Location:
    """Return argmin dist(waypoints to loc)"""
    closest, dist = None, float('inf')
    for l in waypoints:
        if Location.dist(l, loc) < dist:
            dist = Location.dist(l, loc)
            closest = l
    return closest


class Persistence:
    # TODO
    pass
