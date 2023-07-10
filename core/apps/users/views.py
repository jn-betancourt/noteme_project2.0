# REST FRAMEWORK API
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# DJANGO HASHER
import django.contrib.auth.hashers as hasher
from django.contrib.auth.models import User

# MODELS AND SERILIZERS
from .serializers import UserCreationSerializer, UserRetrieveSerializer


class UserCreation(APIView):
    """API view for User actions such us:
    - register a new user
    """

    def post(self, request, format=None):
        """Handles POST request

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """
        status_message = {"detail": "user email or password wrong"}
        status_http = status.HTTP_406_NOT_ACCEPTABLE
        user_info = UserCreationSerializer(
            request.data
        )  # info from  QUERYDICT --> DICT
        email = user_info.data.get("email", None)  # Take the email
        query = User.objects.filter(email=email).first()  # Check if it is register
        if not query:  # If not register --> register new user
            # Create a hash of a password for sec porpuses
            usable_password = hasher.make_password(user_info.data.get("password"))

            new_user = User.objects.create(
                email=email,
                username=user_info.data.get("username"),
                password=usable_password,
            )

            new_user.save()
            token, created = Token.objects.get_or_create(user=new_user)
            status_message = {
                "token": token.key,
                "id": User.objects.filter(email=email).first().id,
                "username": user_info.data.get("username"),
                "email": user_info.data.get("email"),
            }
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)


class UserAuth(APIView):
    """API view for User actions such us:
    - Log In a user
    """

    def post(self, request, format=None):
        """Handles POST request

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """
        status_message = {"detail": "user email or password wrong"}
        status_http = status.HTTP_404_NOT_FOUND

        user = UserRetrieveSerializer(request.data)  # info from QUERYDICT --> DICT
        email = user.data.get("email")
        password = user.data.get("password")
        query = User.objects.get(email=email)  # lookup for the email
        check_password = hasher.check_password(password, query.password) # check the password

        if query and check_password:  # if email and password are correct
            token = Token.objects.get(user=query)
            status_message = {
                "token": token.key,
                "id": query.id,
                "username": query.username,
            }
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
