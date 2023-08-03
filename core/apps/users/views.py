# REST FRAMEWORK API
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# DJANGO HASHER
import django.contrib.auth.hashers as hasher

# MODELS AND SERILIZERS
from .models import NotemeUser
from .serializers import UserCreationSerializer, UserRetrieveSerializer


# The UserCreation class is an API view for creating new users.
class UserCreation(APIView):
    """API view for User actions such us:
    - register a new user
    """

    def post(self, request, format=None):
        """
        The above function handles a POST request to register a new user and returns a response with the
        user's information and a token.

        :param request: The `request` parameter is the Django HTTP request object that contains information
        about the incoming request, such as the request method, headers, and body
        :param format: The `format` parameter is used to specify the format of the response body. It is an
        optional parameter and its default value is `None`. If provided, it can be used to specify the
        desired format of the response, such as JSON, XML, etc
        :return: a Django `Response` object with the `status_message` and `status_http` as the response data
        and status code, respectively.
        """
        status_message = {"detail": "user email or password wrong"}
        status_http = status.HTTP_400_BAD_REQUEST
        user_info = UserCreationSerializer(
            request.data
        )  # info from  QUERYDICT --> DICT
        email = user_info.data["email"]  # Take the email
        query = NotemeUser.objects.filter(pk=email).first()  # Check if it is register
        if not query:  # If not register --> register new user
            # Create a hash of a password for sec porpuses
            usable_password = hasher.make_password(user_info.data["password"])
            new_account = NotemeUser.objects.create(
                email=user_info.data["email"],
                username=user_info.data["username"],
                first_name=user_info.data["first_name"],
                last_name=user_info.data["last_name"],
                password=usable_password,
                provider="NOTEME",
            )
            new_account.save()

            token, _ = Token.objects.get_or_create(user=new_account)
            status_message = {
                "token": token.key,
                "email": new_account.email,
                "username": new_account.username,
            }
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)


# The UserAuth class is an API view for user authentication.
class UserAuth(APIView):
    def post(self, request, format=None):
        """
        This is a Python API view for handling user login requests, where the user provides their email and
        password and the function checks if they are correct and returns a token and user information if
        they are.

        :param request: The `request` parameter is the Django HTTP request object that contains information
        about the incoming request, such as the request method, headers, and body
        :param format: The `format` parameter is used to specify the format of the response body. It can be
        used to indicate whether the response should be in JSON, XML, or any other format supported by the
        API. If not specified, the default format will be used
        :return: The code is returning a Django `Response` object with the `status_message` and
        `status_http` variables as the response data and status code, respectively.
        """
        status_message = {"detail": "user email or password wrong"}
        status_http = status.HTTP_400_BAD_REQUEST

        user = UserRetrieveSerializer(request.data)  # info from QUERYDICT --> DICT
        email = user.data.get("email")
        password = user.data.get("password")

        try:
            query = NotemeUser.objects.get(pk=email)  # lookup for the email
        except:
            return Response(status_message, status_http)

        check_password = hasher.check_password(
            password, query.password
        )  # check the password

        if query and check_password:  # if email and password are correct
            token = Token.objects.get(user=query)
            status_message = {
                "token": token.key,
                "email": email,
                "username": query.username,
            }
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
