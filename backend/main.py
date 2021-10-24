from fastapi import FastAPI

from models import User, TIME_SEGMENTS

app = FastAPI()

user_count = 0

'''
TODOS
Build out the Queue of WalkRequests
- Make an algorithm to pair WalkRequests together to form a trip

Make a Persistence class (see utils) that will persist all relevant objects
Persistence.persist(objs: List[BaseModel]) should write all files into unique files in objects/. See example in models.py/User
Persistence.get(class: BaseModel, key: Any (some identifying component, like an id or name)) should return the relevant object of type class 
''' 



@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/user/")
async def create_user():
    """Create a new user and return their user_id """
    global user_count
    user = User(id=user_count)
    user.write()
    user_count += 1
    return {"user_id": user_count - 1}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    """Return user data for a user_id"""
    user = User.read_from(user_id)
    return user

@app.get("/time_segments/")
async def get_time_segments():
    """Return selectable times"""
    return TIME_SEGMENTS

