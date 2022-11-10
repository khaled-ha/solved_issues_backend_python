from serializers.user_seriliazer import embeddedUserResponse


def postEntity(post) -> dict:
    return {
        'id': str(post['_id']),
        'title': post['title'],
        'category': post['category'],
        'content': post['content'],
        'image': post['image'],
        # 'tags': post['tags'],
        # 'user': str(post['user']),
        'created_at': post['created_at'],
        'updated_at': post['updated_at'],
        'post_rate': post['post_rate'] if 'post_rate' in post.keys() else 0,
    }


def populatedPostEntity(post) -> dict:
    return {
        'id': str(post['id']),
        'title': post['title'],
        'category': post['category'],
        'content': post['content'],
        'image': post['image'],
        # 'user': embeddedUserResponse(post['user']),
        'created_at': post['created_at'],
        'updated_at': post['updated_at'],
        'post_rate': post['post_rate'] if 'post_rate' in post.keys() else 0,
    }


def postListEntity(posts) -> list:
    return [populatedPostEntity(post) for post in posts]
