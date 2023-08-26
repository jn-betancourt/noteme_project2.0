from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import GoogleUsers
from ..usersAuth.models import NotemeUser

# Create your views here.


class GoogleRegister(APIView):
    def post(self, request, format=None):
        status_message = {"detail": "Could not authenticate."}
        status_http = status.HTTP_400_BAD_REQUEST
        user_info = request.data
        query = NotemeUser.objects.filter(pk=user_info["email"]).first()
        # The code block `if user_info.data.get("is_verified") and query:` is checking if the user is
        # verified and if the user exists in the database.
        if user_info["email_verified"] and not query:
            new_account = NotemeUser.objects.create(
                email=user_info["email"],
                username=user_info["name"],
                first_name=user_info["given_name"],
                last_name=user_info["family_name"],
                provider="GOOGLE",
            )
            google_user = GoogleUsers.objects.create(
                account=new_account,
                google_id=user_info["sub"],
                token_id=user_info["jti"],
            )
            new_account.set_unusable_password()
            new_account.save()
            google_user.save()

            token, _ = Token.objects.get_or_create(user=new_account)
            status_http = status.HTTP_200_OK
            status_message = {
                "token": token.key,
                "email": user_info["email"],
                "username": user_info["name"],
            }

        return Response(status_message, status_http)


# The GoogleRegister class is an API view for registering users using Google authentication.
class GoogleLogin(APIView):
    """
    Register a new user to the app

    - receive only a POST request
    """

    def post(self, request, format=None):
        """
        The above function handles the authentication and creation of a new user using Google login.

        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method, headers, body, and query
        parameters
        :param format: The `format` parameter is used to specify the desired format of the response. It
        is set to `None` by default, which means the format will be determined automatically based on
        the request
        :return: The code is returning a response with a status message and status code. The status
        message is a dictionary containing information about the authentication status and user details.
        The status code indicates the success or failure of the authentication process.
        """
        status_message = {"detail": "Could not authenticate."}
        status_http = status.HTTP_400_BAD_REQUEST
        user_info = request.data
        query = NotemeUser.objects.filter(pk=user_info["email"]).first()

        if user_info["email_verified"] and query:
            token = Token.objects.get(user=query)
            google_user = GoogleUsers.objects.get(account=query)
            google_user.token_id = user_info["jti"]
            google_user.save()

            status_message = {
                "token": token.key,
                "username": user_info["name"],
                "email": user_info["email"],
            }
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
