from django.test import TestCase
import django.contrib.auth.hashers as hasher
from rest_framework.test import APIClient

from .models import NotemeUser
from rest_framework.authtoken.models import Token

# Create your tests here.


# The UserTestCase class contains test cases for user sign up and login functionality.
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
        """
        The function `test_signup_user` sends a POST request to the "/api/users/signUp" endpoint with
        user information, and then asserts that the response status code is 200 and the response data
        matches the expected values.
        """
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
        token = Token.objects.get(user=res.data["email"])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            {"token": token.key, "email": "alejo@mail.com", "username": "alejo"},
        )

    def test_wrong_signUp(self):
        """
        The function `test_wrong_signUp` tests the sign up functionality by sending a POST request with
        incorrect email and password, and expects a 400 status code and a specific error message in the
        response.
        """
        res = self.client.post(
            "/api/users/signUp",
            {
                "email": "juan@mail.com",
                "username": "juan08",
                "first_name": "Juan",
                "last_name": "Betancourt",
                "password": "juanito",
            },
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data["detail"], "user email or password wrong")

    def test_login_user(self):
        """
        The function `test_login_user` tests the login functionality by sending a POST request with
        email and password, and then asserts that the response status code is 200 and the response data
        contains a token, email, and username.
        """
        res = self.client.post(
            "/api/users/logIn",
            {"email": "juan@mail.com", "password": "juanito"},
        )
        token = Token.objects.get(user=res.data["email"])
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            {"token": token.key, "email": "juan@mail.com", "username": "juan08"},
        )

    def test_wrong_logIn(self):
        """
        The function tests the logIn endpoint by sending a POST request with a wrong email and password,
        and asserts that the response status code is 400 and the response data detail is "user email or
        password wrong".
        """
        res = self.client.post(
            "/api/users/logIn",
            {"email": "alejo@mail.com", "password": "juanito"},
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            res.data["detail"],
            "user email or password wrong",
        )
