from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4 #unique identifier


#we create an instance of fastapis
app = FastAPI()

#writing a pydantic model that will automatically be converted to JSON data
#this class is going to represent the objects we are passing around throughout this API
class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


#in-memory database (when we turn off our server all our data will be 
#lost but that's okay since this is only testing)   
#tasks here is representing an empty list
tasks = []


#here we set up a simple route with a get endpoint. 
#meaning  we can send get request using the URL in paranthesis
@app.get("/")


#when the get request is sent the function belaow will be triggered
def read():
    #when the function is triggered we're gonna return 
    #this python dictionary. FASTAPI will convert that into JSON data for us
    return{"hello": "world"}


if __name__=="__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)