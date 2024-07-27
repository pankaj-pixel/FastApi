from fastapi import FastAPI
from .Database import  engine
from .import models
from app.routes import post,user,auth,vote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins =["*"]
app.add_middleware(
    CORSMiddleware,
    
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)





























# get post with regular sql
#@app.get("/")
#async def root():
#    cursor.execute("""SELECT * FROM post """)
#    postdata = cursor.fetchall()
#    print(postdata)
#    return postdata



"""@app.post("/posts")
async def get_post(payload: dict = Body()):
    print(payload)
    return {f"Title : {payload['Title'] } Content : {payload['content'] }"}

#Reterive all posts 
@app.post("/posts")

def create_post(post:Post):
    print(post)
    #print(payload.Title)
    #print(payload.content)
    #print(payload.Ratings) 
    print(post.dict())"""
    #return {"data : New Post Created"}"""



"""
@app.post("/posts")
def create_post(post:Post):
    avail_posts = post.dict()
    print(avail_posts)
    avail_posts['id'] = random.randrange(0,1234556)
    my_posts.append(avail_posts)
    print(my_posts)
    return {f"data :{avail_posts}"}
"""

     

#create post using Raw sql
#@app.post("/Create_posts",status_code=status.HTTP_201_CREATED)
#def create_post(post:Post):
#     cursor.execute(""" INSERT INTO post("Title",content,"Published" ) VALUES (%s,%s,%s) RETURNING
#                    * """,(post.Title,post.content,post.Published))
#     newpost = cursor.fetchone()
#     conn.commit()
#     return {"data":newpost}



#get the latest post added
"""@app.get("/post/latest")
def get_the_latest_post():
    post = my_posts[len(my_posts)-1]
    print(post)
    return post
"""


#get post by id 
"""@app.get("/posts/{id}",status_code=status.HTTP_201_CREATED)
def retrieve_post_by_id(id:int):
    for post in my_posts:
        print(post)
        if post["id"] == id:
            print(post["id"])
            return post
        if not post:
            return { status.HTTP_404_NOT_FOUND }
    # If the loop completes without finding the post, raise HTTPException with 404 Not Found
    raise HTTPException(status_code = 404, detail="Post not found")

"""






#get post by id using database
#@app.get("/posts/{id}",status_code=status.HTTP_200_OK)
#def retrieve_post_by_id(id:int):
#        cursor.execute("""SELECT *  FROM public.post WHERE id = %s """,(str(id),))
#        id_data = cursor.fetchone()
#        print(id_data)
#        # Check if id_data is None (no data found)
#        if id_data is None:
#            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post found with id {id}")
#        Return the fetched data
#        return id_data




#get post by id using SQLALCHEMY



#Delete post by id using sqlAlchemy




#Delete post by id 
#@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
#def delete_postby_id(id:int): 
#        cursor.execute("""DELETE FROM post WHERE id = %s """,(str(id),))
#        conn.commit()
#        if not id:
#             return HTTPException(status_code=404,detail= f"Post {id} Doesnot Exist")
#        return {"message": f"Post with id {id} has been successfully deleted"}
    


#update post
"""@app.put("/posts/{id}",status_code=204)
def update_request(id:int,post:Post):
    index = Find_index(id)
    if index == None:
        return HTTPException(status_code=404,detail="Post Doesnot Exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {f"data : {my_posts}"}

"""



#update post in database through api

#update post in database through api
#@app.put("/update_posts/{id}",status_code=204)
#def update_request(id:int,post:Post):
#    cursor.execute("""UPDATE public.post SET "Title" = %s ,content =%s ,"Published" = %s WHERE id = %s RETURNING * """,(post.Title, post.content, post.Published ,str(id)))
#    updatespost = cursor.fetchone()
#    conn.commit()
#    if updatespost == None:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id Not Found !!!") 
#    return{"Data ": updatespost}


