from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import csv
import hashlib
import uvicorn


class Info(BaseModel):
    firstname: str
    lastname: str


app = FastAPI()

user_details  = {
    29:{
        "firstname":"john",
        "lastname": "smith",
    },
    30:{
        "firstname":"john",
        "lastname":"doe"
    }
    

}


def writer(credential):
    with open("/records.csv", 'w') as file:#change directory of csv file to your system location
        writer = csv.writer(file)
        writer.writerow(credential)

@app.post("/create-user/{person_id}")
def create_user(person_id: int, credential: Info):
    if person_id in user_details :
        return {"Error": "User ID already exists"}
    
    # user_details[person_id] = {"firstname":credential.firstname.encode(), "lastname":credential.lastname.encode()}
    user_details[person_id] = writer(f'{hashlib.sha256(credential.firstname.encode())}\n {hashlib.sha256(credential.lastname.encode())}')
    return user_details[person_id]


if __name__ == '__main__':
    uvicorn.run(app)



  
#TODO
# @app.get("/get-person/{person_id}")
# def get_user(person_id: int = Path(None, description="The ID of the item you like to view", gt=0, lt=100)):
#     return user_details[person_id]

# @app.get("/get-by-name/{person_id}")
# def get_user(*, person_id: int,  name: Optional[str] = None, test:int ):
#     for person in user_details:
#         if user_details[person].firstname == name:
#             return user_details[person]
#     return {"User": "Not found"}

# @app.get('/')
# def user_info():
#     return {"user_info":"something else"}

# @app.get('/about')
# def about():
#     return {"Dummy":"Data"}

# @app.post("/create-user")
# def create_user(detail:Info):
#     return 


