from django.test import TestCase
from django.urls import reverse

from user_post.forms import UsersPostCreateForm
from user_post.models import UsersPosts, Usersjson


class UsersPostsTestsCase(TestCase):
    fixtures = [
        "userpost.fixture.json",
        "userjson.fixture.json",
        "postsjson.fixture.json"
    ]

    def test_list_users(self):
        response = self.client.get(reverse("user_post:list"))
        self.assertEqual(response.status_code, 200)

        userpost = UsersPosts.objects.all()
        userpost_in_context = response.context["usersposts"]
        self.assertEqual(len(userpost), len(userpost_in_context))
    def test_json_users(self):
        post = Usersjson.objects.get(pk=1)
        self.assertEqual(post.name, "Leanne Graham")



class DetailViewTestsCase(TestCase):
    fixtures = [
        "userpost.fixture.json",
    ]

    def test_detail(self):
        userpost = UsersPosts.objects.first()
        response = self.client.get(reverse("user_post:details",kwargs={'pk': userpost.pk}))
        self.assertEqual(response.status_code, 200)
    def test_detail_404(self):
        response = self.client.get(reverse("user_post:details", kwargs={'pk': 20}))
        self.assertEqual(response.status_code, 404)