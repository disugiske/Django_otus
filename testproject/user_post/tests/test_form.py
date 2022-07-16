from django.test import TestCase
from django.urls import reverse

from user_post.forms import UsersPostCreateForm


class CreateFormTestsCase(TestCase):
    fixtures = [
        "userpost.fixture.json",
    ]
    def test_form(self):
        response = self.client.get(reverse("user_post:create"))
        self.assertEqual(response.status_code, 200)

    def test_form_isvalid(self):
        data = {"name": "bulochka", "username": "bulk", "email": "jrigjrij@ufjffh.ru", "address": "", "body": "orjgorjgoerjgerger"}
        form = UsersPostCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        data = {"name": "", "username": "bulk", "email": "jrigjrijufjffh.ru", "address": "",
                "body": "orjgorjgoerjgerger"}
        form = UsersPostCreateForm(data=data)
        self.assertFalse(form.is_valid())