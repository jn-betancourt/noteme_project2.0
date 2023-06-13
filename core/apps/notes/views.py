# REST FRAMEWORD API UTILS
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# SERIALIZER FOR NOTES
from .serializers import NotesSerializer

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
        status_http = status.HTTP_404_NOT_FOUND

        user_id = request.data.get("id")  # require the id of the user
        query = Note.objects.filter(user_id=user_id)
        notes = []

        if query:  # if user exist
            for note in query:  # take each note from QUERYSET --> DICT
                info_note = NotesSerializer(note)
                nota_format = {
                    "id": info_note.data.get("id"),
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
        status_message = {"detail": "Authentication credentials were not provided."}
        status_http = status.HTTP_406_NOT_ACCEPTABLE

        action = request.headers.get("action")

        if action == "POST":  # if header "action" set to POST
            note_info = NotesSerializer(request.data)  # gather the note info
            query = User.objects.get(pk=note_info.data.get("id"))  # gather user id

            if query:
                new_note = Note.objects.create(
                    title=note_info.data.get("title"),
                    description=note_info.data.get("description"),
                    user_id=query,
                )
                new_note.save()  # save new note

                status_message = {"response": {"id": new_note.id}}
                status_http = status.HTTP_201_CREATED

        if action == "DELETE":  # if header "action" set to DELETE
            id_note = request.data.get("id")  # id of the note
            query = Note.objects.get(pk=id_note)

            if query:
                query.delete(keep_parents=True)

                status_message = {"response": {"message": "Note deleted"}}
                status_http = status.HTTP_200_OK

        if action == "PUT":  # if header "action" set to PUT
            note_info = NotesSerializer(request.data)  # gather the note new info
            id_note = note_info.data.get("id")
            query = Note.objects.get(pk=id_note)

            if query:
                query.title = str(note_info.data.get("title"))
                query.description = str(note_info.data.get("description"))

                query.save()

                status_message = {"response": {"message": "Note modified"}}
                status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
