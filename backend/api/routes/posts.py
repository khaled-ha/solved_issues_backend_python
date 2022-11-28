from fastapi import APIRouter, Body
from methodes.posts import (
    add_post,
    delete_post,
    rate_post_by_id,
    retrieve_post,
    retrieve_posts,
    update_post,
)
from validators.post_validators import (
    CreatePostSchema,
    ErrorResponseModel,
    ResponseModel,
    UpdatePostSchema,
)
from fastapi.encoders import jsonable_encoder

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
def update_post_data(id: str, req: UpdatePostSchema = Body(...)):
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


@post_router.delete('/{id}', response_description='post data deleted from the database')
def delete_post_data(id: str):
    deleted_post = delete_post(id)
    if deleted_post:
        return ResponseModel(
            'post with ID: {} removed'.format(id), 'post deleted successfully'
        )
    return ErrorResponseModel(
        'An error occurred', 404, "post with id {} doesn't exist".format(id)
    )


@post_router.post('/{id}/rate', response_description='rate post')
async def rate_post(id: str):
    if rate_post_by_id(id):
        return ResponseModel(
            'post with ID: {} rated'.format(id), 'post rated successfully'
        )
    return ErrorResponseModel(
        'An error occurred', 404, "post with id {} doesn't exist".format(id)
    )
