# REST FRAMEWORK API
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

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

        status_message = {"message": "user email or password wrong"}
        status_http = status.HTTP_404_NOT_FOUND

        user = UserRetrieveSerializer(request.data)  # info from QUERYDICT --> DICT
        email = user.data.get("email")
        password = user.data.get("password")
        query = Users.objects.filter(email=email).first()  # lookup for the email

        if query and password == query.password:  # if email and password are correct
            status_message["message"] = "user found"
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)

    def post(self, request, format=None):
        """Handles POST request

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """

        status_message = {"message": "user email or password wrong"}
        status_http = status.HTTP_406_NOT_ACCEPTABLE

        user_info = UserCreationSerializer(
            request.data
        )  # info from  QUERYDICT --> DICT
        email = user_info.data.get("email", None)  # Take the email
        query = Users.objects.filter(email=email).first()  # Check if it is register

        if not query:  # If not register --> register new user
            status_message = {"message": "successful creation"}
            status_http = status.HTTP_201_CREATED
            new_user = Users.objects.create(
                email=email,
                name=user_info.data.get("name"),
                password=user_info.data.get("password"),
            )
            new_user.save()

        return Response(status_message, status_http)
