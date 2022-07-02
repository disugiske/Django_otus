from .models import Usersjson, Postsjson

import requests

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    postdata = requests.get(POSTS_DATA_URL).json()
    return postdata

def get_userdata():
    userdata = requests.get(USERS_DATA_URL).json()
    return userdata


def load_json_users(userdata, postdata):
    user_json = []
    post_json = []
    for list_data in userdata:
        user_json.append(Usersjson(
            name=list_data.get("name"),
            username=list_data.get("username"),
            email=list_data.get("email"),
            pk=list_data.get("id"),
        )
        )
    Usersjson.objects.bulk_create(user_json)
    for post_data in postdata:
        post_json.append(Postsjson(
            userId_id=post_data.get("userId"),
            body=post_data.get("body"))
        )
    Postsjson.objects.bulk_create(post_json)

    print(user_json)



def init():
    if not Usersjson.objects.all().exists():
        load_json_users(get_userdata(), get_posts())
