from django.test import TestCase
from rest_framework.test import APIClient

from .models import GoogleUsers
from ..users.models import NotemeUser

# Create your tests here.


class GoogleUsersTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "iss": "https://accounts.google.com",
            "azp": "387937601630-4qp9i2826864vtld90buqp34rv6k8bh7.apps.googleusercontent.com",
            "aud": "387937601630-4qp9i2826864vtld90buqp34rv6k8bh7.apps.googleusercontent.com",
            "sub": "115642388832183751935",
            "email": "jantonito@gmail.com",
            "email_verified": True,
            "nbf": 1691009131,
            "name": "Juan Antonio Betancourth Parra",
            "picture": "https://lh3.googleusercontent.com/a/AAcHTte4ju9CRGZPI4IwfjK4QdSilE9Rbz1J_zQ1jFsLDPlM=s96-c",
            "given_name": "Juan Antonio",
            "family_name": "Betancourth Parra",
            "locale": "es",
            "iat": 1691009431,
            "exp": 1691013031,
            "jti": "bdfee0adec2d5ba350a4c1bf69043a1337",
        }
        # user = NotemeUser.objects.create(
        #     email=self.data["email"],
        #     username=self.data["name"],
        #     first_name=self.data["given_name"],
        #     last_name=self.data["family_name"],
        # )
        # user.set_unusable_password()
        # GoogleUsers.objects.create(
        #     account_id=user, google_id=self.data["sub"], token_id=self.data["jti"]
        # )

    def test_register(self):
        res = self.client.post("/api/google/register", self.data)
        self.assertEqual(res.status_code, 200)
