from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response, Body
from pymongo.collection import ReturnDocument
from config.mongo_config import Post
from methodes.posts import add_post, retrieve_post, retrieve_posts
from validators.post_validators import (
    CreatePostSchema,
    ErrorResponseModel,
    ResponseModel,
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
