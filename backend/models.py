from __future__ import annotations

from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
import logging
from typing import Optional, List, Dict
from pydantic import BaseModel

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

# ---! !---

class User(BaseModel):
    """User class"""
    name: str
    id: Optional[int] = None

    @staticmethod
    def read_from(id: int) -> User:
        pass

    @staticmethod
    def from_local(id: int) -> User:
        pass

    def write(self):
        pass

    def write_local(self) -> Path:
        pass

    
class Location(BaseModel):
    # we need to know the navigation api we're using, Location will be represented in that
    pass

class WalkRequest(BaseModel):
    requester: User
    from_loc: Location
    to_loc: Location
    time: int # placeholder