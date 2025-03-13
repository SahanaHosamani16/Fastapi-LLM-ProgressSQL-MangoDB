from fastapi import FastAPI
from . import  models
from .database import engine
from .routers import blog,user,authentication


app=FastAPI()

models.Base.metadata.create_all(engine)  #to create a table in database
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
# def get_db():
#     db = SessionLocal()
#     try:app.include_router(user.router)
#         yield db
#     finally:
#         db.close()

 #post  



# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create(request:schemas.Blog,db:Session = Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)  #sql alchamy model
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog




    


   

    