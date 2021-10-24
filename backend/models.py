from __future__ import annotations
import datetime
import math

from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
import logging
from typing import Any, Optional, List, Dict
from pydantic import BaseModel
import jsons

# subsumed by pydantic BaseModel
# from dataclasses import dataclass


# ---! basic initialization !---
LOCAL_OBJECT_PATH = Path('objects/')
PATHS = [LOCAL_OBJECT_PATH]
def init_paths():
    for p in PATHS:
        if not p.exists():
            p.mkdir()
            logging.info(f'{p} made')
        else:
            logging.info(f'{p} exists')

init_paths()

TIME_SEGMENTS = [i for i in range(24)]

# ---! !---

class User(BaseModel):
    """User class"""
    id: int

    @staticmethod
    def read_from(id: int) -> User:
        return User.from_local(id)

    @staticmethod
    def from_local(id: int) -> User:
        # here is an example of deserializing a file. keep all objects in the LOCAL_OBJECT_PATH and then read them as an object. In this case the unique identifying key is the id, hashes also work
        local_path = LOCAL_OBJECT_PATH / str(id)
        if local_path.exists():
            # with open(local_path, 'r') as fp:
            user = User.parse_file(local_path)
            return user
        raise Exception('no matching Instance found')

    def write(self):
        return self.write_local()

    def write_local(self) -> Path:
        local_path = LOCAL_OBJECT_PATH / str(self.id)
        if local_path.exists():
            logging.info(f'Path {str(local_path)} already exists for User {str(self)}, overwriting')
        with open(local_path, 'w') as fp:
            fp.write(self.json())
        return local_path

    
class Location(BaseModel):
    name: Optional[str] = None
    startpt: Optional[bool] = True
    endpt: Optional[bool] = True
    lat: Optional[float]
    lng: Optional[float]

    @staticmethod
    def dist(a: Location, b: Location):
        return math.dist([a.lat, a.lng], [b.lat, b.lng])


class WalkRequest(BaseModel):
    requester: User
    from_loc: Location
    to_loc: Location
    # placeholder
    time: Any 

class Queue(BaseModel):
    queue = {} # times : list of walkrequests

    def insert(r: WalkRequest):
        if (Queue.queue.get(r.time) == None):
            walkers = []
        else:
            walkers = Queue.queue.get(r.time)
        walkers.append(r)
        Queue.queue.update({r.time: walkers})

    def delete() -> List(WalkRequest):
        soonest_time = min(Queue.queue.keys) 
        return Queue.queue.pop(soonest_time)


    #do we want to group by some range of times? 
    #or will the time within the walk request be set to a specific set of times so that we don't have to worry about grouping like that?
    #do we need to take into account users they do not want to be grouped with? How to get this info?
    #need to take the first group off the queue when their departure time is next
    #how to take care of arrival vs departure time? Do we have both options or not?
    #is it better to use an OrderedDict so that the times will already be ordered? 

