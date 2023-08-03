from django.test import TestCase
import django.contrib.auth.hashers as hasher
from rest_framework.test import APIClient

from .models import NotemeUser

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        usable_password = hasher.make_password("juanito")
        NotemeUser.objects.create(
            email="juan@mail.com",
            username="juan08",
            first_name="Juan",
            last_name="Betancourt",
            password=usable_password,
        )

    def test_signup_user(self):
        res = self.client.post(
            "/api/users/signUp",
            {
                "username": "alejo",
                "password": "alejo1",
                "email": "alejo@mail.com",
                "first_name": "Alejandro",
                "last_name": "Betancourt",
            },
        )        
        self.assertEqual(res.status_code, 200)

    def test_login_user(self):
        res = self.client.post(
            "/api/users/logIn",
            {"email": "juan@mail.com", "password": "juanito"},
        )
        self.assertEqual(res.status_code, 200)
