from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import GoogleAccountSerializer
from .models import GoogleAccount
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.


class GoogleRegister(APIView):
    """
    Register a new user to the app

    - receive only a POST request
    """

    def post(self, request, format=None):
        # generic status messages
        status_message = {"detail": "Authentication credentials were wrong."}
        status_http = status.HTTP_400_BAD_REQUEST
        user_info = GoogleAccountSerializer(request.data)
        query = GoogleAccount.objects.filter(email=user_info.data["email"]).first()

        if user_info.data.get("is_verified") and not query:
            google_user = GoogleAccount.objects.create(**user_info.data)
            new_user = User.objects.create(
                username=user_info.data["username"],
                email=user_info.data["email"],
            )
            new_user.save()
            google_user.save()

            token, _ = Token.objects.get_or_create(user=new_user)
            status_http = status.HTTP_200_OK
            status_message = {
                "token": token.key,
                "id": new_user.id,
                "username": user_info.data["username"],
                "email": user_info.data["email"],
                "picture": user_info.data["picture"],
            }

        return Response(status_message, status_http)


class GoogleLogin(APIView):
    """
    Login a new user to the app

    - receive only a POST request
    """

    def post(self, request, format=None):
        # generic status messages
        status_message = {"detail": "No Account Found."}
        status_http = status.HTTP_400_BAD_REQUEST
        user_info = GoogleAccountSerializer(request.data)
        query = get_object_or_404(User, email=user_info.data["email"])

        if user_info.data.get("is_verified") and query:
            token = Token.objects.get(user=query)
            status_http = status.HTTP_200_OK
            status_message = {
                "token": token.key,
                "id": query.id,
                "username": user_info.data["username"],
                "email": user_info.data["email"],
                "picture": user_info.data["picture"],
            }

        return Response(status_message, status_http)
