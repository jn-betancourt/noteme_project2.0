# REST FRAMEWORD API UTILS
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# SERIALIZER FOR NOTES
from .serializers import NoteSerializer

# MODELS FOR NOTES
from .models import Note
from ..users.models import NotemeUser


# The `NotesManagement` class is a base API class for managing notes, allowing users to retrieve,
# create, update, and delete notes.
class NotesManagement(APIView):
    """Base API class for notes management

    HTTP method allowed
        GET, POST, PUT, DELETE
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        """
        This function retrieves notes belonging to a user and returns them in a response.

        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, and
        query parameters
        :param format: The `format` parameter is used to specify the desired format of the response
        data. It is set to `None` by default, which means the format will be determined automatically
        based on the request's `Accept` header
        :return: a Response object with the status message and status code.
        """

        # generic status messages
        status_message = {"detail": "Authentication credentials were not provided."}
        status_http = status.HTTP_204_NO_CONTENT
        user_email = request.user.email  # require the email of the user
        query = Note.objects.filter(account=user_email)
        notes = []

        if query:  # if user exist
            for note in query:  # take each note from QUERYSET --> DICT
                info_note = NoteSerializer(note)
                note_format = {
                    "note_id": info_note.data.get("note_id"),
                    "title": info_note.data.get("title"),
                    "description": info_note.data.get("description"),
                }
                notes.append(note_format)  # append the note converted to the list

            status_message = {"response": notes}
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)

    def post(self, request, format=None):
        """
        The above function is a Django view that handles the POST request to create a new note.

        :param request: The `request` parameter is an instance of the Django `HttpRequest` class, which
        represents the HTTP request made by the client
        :param format: The `format` parameter is used to specify the format of the request body. It can
        be used to indicate whether the request body is in JSON, XML, or any other format. In this case,
        the `format` parameter is not used in the code snippet provided
        :return: The code is returning a Django Response object with a status message and HTTP status
        code. The status message is a dictionary with a key "detail" and value "note created". The HTTP
        status code is 201 (status.HTTP_201_CREATED).
        """
        note_info = NoteSerializer(request.data, read_only=True)  # gather the note info
        query = NotemeUser.objects.get(pk=request.user.email)  # gather user pk
        new_note = Note.objects.create(
            note_id=note_info.data.get("note_id"),
            title=note_info.data.get("title"),
            description=note_info.data.get("description"),
            account=query,
        )
        new_note.save()  # save new note

        status_message = {"datail": "note created"}
        status_http = status.HTTP_201_CREATED

        return Response(status_message, status_http)

    def put(self, request, format=None):
        """
        The above function is a PUT method in Python that updates the values of a note object.

        :param request: The `request` parameter is the Django HTTP request object that contains
        information about the incoming request, such as the request method, headers, and body
        :param format: The `format` parameter is used to specify the format of the request body. It can
        be used to indicate whether the request body is in JSON, XML, or any other format
        :return: a Django Response object with a status message of "Note modified" and a status code of
        201 (HTTP_CREATED).
        """

        note_info = NoteSerializer(request.data)  # gather the note new info
        note_id = note_info.data.get("note_id")
        query = Note.objects.get(pk=note_id)  # retrieve the note store
        # UPDATE THE NOTE VALUES
        query.title = str(note_info.data.get("title"))
        query.description = str(note_info.data.get("description"))

        query.save()

        status_message = {"message": "Note modified"}
        status_http = status.HTTP_201_CREATED

        return Response(status_message, status_http)

    def delete(self, request, format=None):
        """
        This function deletes a note from the database based on the provided note_id.

        :param request: The `request` parameter is an object that contains information about the current
        HTTP request. It includes details such as the request method, headers, and data
        :param format: The "format" parameter is used to specify the desired format of the response. It
        is typically used when working with APIs that support multiple response formats, such as JSON,
        XML, or HTML. By default, the format is set to None, which means the response format will be
        determined based on the
        :return: The code is returning a Response object with a status message and status code. The
        status message is "Note deleted" and the status code is 200 (HTTP_OK).
        """

        note_id = request.data.get("note_id")  # id of the note
        query = Note.objects.get(pk=note_id)
        query.delete(keep_parents=True)  # delete note, prevent del parent

        status_message = {"message": "Note deleted"}
        status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
