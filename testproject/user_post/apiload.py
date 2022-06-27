import requests
from django.http import request

from models import Usersjson, Postsjson

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

qweryset = Usersjson.object.all()
if qweryset.exists() == False:
    def get_userdata():
        userdata = requests.get(USERS_DATA_URL).json()
        return userdata

    def get_posts():
        postdata = requests.get(POSTS_DATA_URL).json()
        return postdata


    def load_json_users(userdata, postdata):
        for list_data in userdata:
            user_json.append(Usersjson(
                name=list_data.get("name"),
                username=list_data.get("username"),
                email=list_data.get("email"),
                user_id=list_data.get("id"),
                                    )
            )
        Usersjson.object.bulk_create(user_json)

        for post_data in postdata:
            post_json.append(Postsjson(
                user_id=post_data.get("userId"),
                body=post_data.get("body"))
            )
        Postsjson.object.bulk_create(post_json)
