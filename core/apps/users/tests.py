from django.test import TestCase
from django.contrib.auth.models import User
import django.contrib.auth.hashers as hasher
from rest_framework.test import APIClient

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self) -> None:
        usable_password = hasher.make_password("juanito")
        User.objects.create(
            email="juan@mail.com", username="juan", password=usable_password
        )

    def test_signup_user(self):
        client = APIClient()
        res = client.post(
            "/api/users/signUp",
            {"username": "alejo", "password": "alejo", "email": "alejo@mail.com"},
            format="json",
        )
        self.assertEqual(res.status_code, 200)

    def test_login_user(self):
        client = APIClient()
        res = client.post(
            "/api/users/logIn",
            {"email": "juan@mail.com", "password": "juanito"},
            format="json",
        )
        self.assertEqual(res.status_code, 200)
