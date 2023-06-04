# REST FRAMEWORK API
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

# DJANGO HASHER
import django.contrib.auth.hashers as hasher

# MODELS AND SERILIZERS
from .serializers import UserCreationSerializer, UserRetrieveSerializer
from .models import Users


class UserManagement(APIView):
    """API view for users actions such us:
    - log in
    - register
    """

    def get(self, request, format=None):
        """Handles GET request

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """

        status_message = {"response": "user email or password wrong"}
        status_http = status.HTTP_404_NOT_FOUND

        user = UserRetrieveSerializer(request.data)  # info from QUERYDICT --> DICT
        email = user.data.get("email")
        password = user.data.get("password")

        query = Users.objects.filter(email=email).first()  # lookup for the email
        check_password = hasher.check_password(password, query.password)

        if query and check_password:  # if email and password are correct
            status_message = {
                "response": {"id": query.id, "name": query.name, "email": query.email}
            }
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)

    def post(self, request, format=None):
        """Handles POST request

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """

        status_message = {"response": "user email or password wrong"}
        status_http = status.HTTP_406_NOT_ACCEPTABLE

        user_info = UserCreationSerializer(
            request.data
        )  # info from  QUERYDICT --> DICT
        email = user_info.data.get("email", None)  # Take the email
        query = Users.objects.filter(email=email).first()  # Check if it is register

        if not query:  # If not register --> register new user
            # Create a hash of a password for sec porpuses
            usable_password = hasher.make_password(user_info.data.get("password"))
            new_user = Users.objects.create(
                email=email,
                name=user_info.data.get("name"),
                password=usable_password,
            )
            new_user.save()
            status_message = {
                "response": {
                    "id": Users.objects.filter(email=email).first().id,
                    "name": user_info.data.get("name"),
                    "email": user_info.data.get("email"),
                }
            }
            status_http = status.HTTP_201_CREATED

        return Response(status_message, status_http)
