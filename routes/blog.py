from fastapi import APIRouter
from models.blog import BlogModel , UpdateBlogModel
from config.config import blog_collection
from serializers.blog import decode_blogs , decode_blog
from bson import ObjectId
import datetime

blog_root = APIRouter()

#post requst
@blog_root.post("/new/blog")

def new_blog(doc:BlogModel):
    doc = dict(doc)
    current_date = datetime.date.today()
    doc["date"] = str(current_date)
    res = blog_collection.insert_one(doc)
    doc_id = str(res.inserted_id)
    return {
        "status" : "ok",
        "message" : "Blog posted successfully",
        "_id" : doc_id
    }

@blog_root.get('/all/blogs')
def all_blogs():
    res = blog_collection.find()
    decoded_data = decode_blogs(res)

    return {
        "status" : "ok",
        "data" : decoded_data
    }


@blog_root.get("/blog/{_id}")
def get_blog(_id:str):
    res = blog_collection.find_one({
        "_id" : ObjectId(_id)
    })
    decoded_blog = decode_blog(res)
    return {
        "status" : "ok",
        "data" : decoded_blog
    }


#Update blog
@blog_root.patch("/update/{_id}")

def update_blog(_id: str, doc:UpdateBlogModel):
    res = dict(doc.model_dump(exclude_unset=True))

    blog_collection.find_one_and_update({
        "_id": ObjectId(_id)},
        {"$set" : res}
    )
    return {
        "status" : "ok",
        "message" : "blog updated successfully"
    }

@blog_root.delete("/delect{_id}")
def delete_blog(_id : str):
    blog_collection.find_one_and_delete(
        {"_id" : ObjectId(_id)}
    )

    return {
        "ststus" : "ok",
        "message": "Blog deleted successfuly"
    }