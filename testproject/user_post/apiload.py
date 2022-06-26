import requests
from django.http import request

from models import Usersjson, Postsjson

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


def get_userdata():
    userdata = requests.get(USERS_DATA_URL).json()
    return userdata


def get_posts():
    postdata = requests.get(POSTS_DATA_URL).json()
    return postdata


users_data, posts_data = get_userdata(), get_posts()


def load_json_users():
    for list_data in users_data:
        user_json = Usersjson(
            name=list_data.get("name"),
            username=list_data.get("username"),
            email=list_data.get("email"),
            user_id=list_data.get("id"),
        )
        user_load = request.session.get('user_json')

    for post_data in posts_data:
        post_json = Postsjson(user_id=post_data.get("userId"), body=post_data.get("body"))
        db.session.add(post_json)
    db.session.commit()
