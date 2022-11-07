from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response, Body
from pymongo.collection import ReturnDocument
from config.mongo_config import Post
from methodes.posts import add_post, retrieve_post, retrieve_posts, update_post
from validators.post_validators import (
    CreatePostSchema,
    ErrorResponseModel,
    ResponseModel,
    UpdatePostSchema,
)
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

post_router = APIRouter()


@post_router.post('/', response_description='Post data added into the database')
def add_post_data(post: CreatePostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = add_post(post)
    return ResponseModel(new_post, 'Post added successfully.')


@post_router.get('/', response_description='Posts retrieved')
def get_posts():
    posts = retrieve_posts()
    if posts:
        return ResponseModel(posts, 'Posts data retrieved successfully')
    return ResponseModel(posts, 'Empty list returned')


@post_router.get('/{id}', response_description='Post data retrieved')
def get_post_data(id):
    post = retrieve_post(id)
    if post:
        return ResponseModel(post, 'Post data retrieved successfully')
    return ErrorResponseModel('An error occurred.', 404, "Post doesn't exist.")


@post_router.put('/{id}')
async def update_post_data(id: str, req: UpdatePostSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_post = update_post(id, req)
    if updated_post:
        return ResponseModel(
            'post with ID: {} name update is successful'.format(id),
            'post updated successfully',
        )
    return ErrorResponseModel(
        'An error occurred',
        404,
        'There was an error updating the post data.',
    )
