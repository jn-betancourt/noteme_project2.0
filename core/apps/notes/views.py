# REST FRAMEWORD API UTILS
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# SERIALIZER FOR NOTES
from .serializers import NoteSerializer

# MODELS FOR NOTES
from .models import *
from django.contrib.auth.models import User


class NotesManagement(APIView):
    """Base API class for notes management

    HTTP methods allowed:
        GET, POST
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        """GET method

        HTTP method allowed:
            GET

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """
        # generic status messages
        status_message = {"detail": "Authentication credentials were not provided."}
        status_http = status.HTTP_204_NO_CONTENT
        user_id = request.headers.get("id")  # require the id of the user
        query = Note.objects.filter(user_id_id=user_id)
        notes = []

        if query:  # if user exist
            for note in query:  # take each note from QUERYSET --> DICT
                info_note = NoteSerializer(note)
                nota_format = {
                    "note_id": info_note.data.get("note_id"),
                    "title": info_note.data.get("title"),
                    "description": info_note.data.get("description"),
                }
                notes.append(nota_format)  # append the note converted to the list

            status_message = {"response": notes}
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)

    def post(self, request, format=None):
        """POST method

        HTTP method allowed
            POST, PUT, DELETE

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """
        status_message = {"detail": "Action header not specified."}
        status_http = status.HTTP_406_NOT_ACCEPTABLE

        action = request.headers.get("action")
        if action == "POST":  # if header "action" set to POST
            note_info = NoteSerializer(
                request.data, read_only=True
            )  # gather the note info
            query = User.objects.get(pk=note_info.data.get("id"))  # gather user id
            new_note = Note.objects.create(
                note_id=note_info.data.get("note_id"),
                title=note_info.data.get("title"),
                description=note_info.data.get("description"),
                user_id=query,
            )
            new_note.save()  # save new note
            status_message = {"datail": "note created"}
            status_http = status.HTTP_201_CREATED

        if action == "PUT":  # if header "action" set to PUT
            note_info = NoteSerializer(request.data)  # gather the note new info
            note_id = note_info.data.get("note_id")
            query = Note.objects.get(note_id=note_id)

            query.title = str(note_info.data.get("title"))
            query.description = str(note_info.data.get("description"))

            query.save()

            status_message = {"message": "Note modified"}
            status_http = status.HTTP_200_OK

        if action == "DELETE":  # if header "action" set to DELETE
            note_id = request.data.get("note_id")  # id of the note
            query = Note.objects.get(note_id=note_id)
            query.delete(keep_parents=True)

            status_message = {"message": "Note deleted"}
            status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
