# Retrieve all posts present in the database
from config.mongo_config import Post
from serializers.post_serilizers import postEntity, postListEntity
from bson.objectid import ObjectId


def retrieve_posts():
    posts = []
    for post in Post.find():
        posts.append(postEntity(post))
    print(posts)
    return postListEntity(posts)


# Add a new post into to the database
def add_post(post_data: dict) -> dict:
    print(post_data)
    post = Post.insert_one(post_data)
    new_post = Post.find_one({'_id': post.inserted_id})
    return postEntity(new_post)


# Retrieve a post with a matching ID
def retrieve_post(id: str) -> dict:
    post = Post.find_one({'_id': ObjectId(id)})
    if post:
        return postEntity(post)


# Update a post with a matching ID
def update_post(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    post = Post.find_one({'_id': ObjectId(id)})
    if post:
        updated_post = Post.update_one({'_id': ObjectId(id)}, {'$set': data})
        if updated_post:
            return True
        return False


# Delete a post from the database
def delete_post(id: str):
    post = Post.find_one({'_id': ObjectId(id)})
    if post:
        Post.delete_one({'_id': ObjectId(id)})
        return True
