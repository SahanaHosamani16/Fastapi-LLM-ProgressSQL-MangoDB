from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app=FastAPI()

@app.get('/blog')   #first api(decorate)
def index(limit=10,published:bool=True,sort: Optional[str]=None):
    #only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db list '}
    else:
        return {'data': f'{limit}  blogs from the db list '}

@app.get('/blog/unpublished')
def unpublished():
    return{'data':'all unpublished blogs'}


@app.get('/blog/{id}')   #{} for dynamic routing
def show(id:int):
    return{'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id=id
    return{'data':{'1','2'}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
   

@app.post('/blog')
def create_blog(request: Blog):
    return{'data': f"Blog is created with title as {request.title}"}



 


