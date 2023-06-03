# REST FRAMEWORD API UTILS
from rest_framework.views import APIView, Response, status

# SERIALIZER FOR NOTES
from .serializers import NotesSerializer

# MODELS FOR NOTES
from .models import *
from ..users.models import Users


class NotesManagement(APIView):
    """Base API class for notes management

    HTTP methods allowed:
        GET, POST
    """

    def get(self, request, format=None):
        """GET method

        HTTP method allowed:
            GET

        Args:
            request: First argument Django http base class provide.
            format: Body format.
        """
        status_message = {"response": "No notes found"}
        status_http = status.HTTP_404_NOT_FOUND

        user_id = request.data.get("id")
        query = Notes.objects.filter(user_id=user_id)
        notes = []
        if query:
            for note in query:
                info_note = NotesSerializer(note)
                nota_format = {
                    "id": info_note.data.get("id"),
                    "title": info_note.data.get("title"),
                    "description": info_note.data.get("description"),
                }
                notes.append(nota_format)

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
        status_message = {"response": "generic post method"}
        status_http = status.HTTP_406_NOT_ACCEPTABLE

        action = request.headers.get("action")

        if action == "POST":
            user_info = NotesSerializer(request.data)
            query = Users.objects.get(pk=user_info.data.get("id"))

            if query:
                new_note = Notes.objects.create(
                    title=user_info.data.get("title"),
                    description=user_info.data.get("description"),
                    user_id=query,
                )
                new_note.save()

                status_message = {"response": {"id": new_note.id}}
                status_http = status.HTTP_201_CREATED

        if action == "DELETE":
            id_note = request.data.get("id")
            query = Notes.objects.get(pk=id_note)

            if query:
                query.delete(keep_parents=True)

                status_message = {"response": {"message": "Note deleted"}}
                status_http = status.HTTP_200_OK

        if action == "PUT":
            note_info = NotesSerializer(request.data)
            id_note = note_info.data.get("id")
            query = Notes.objects.get(pk=id_note)

            if query:
                query.title = str(note_info.data.get("title"))
                query.description = str(note_info.data.get("description"))

                query.save()

                status_message = {"response": {"message": "Note modified"}}
                status_http = status.HTTP_200_OK

        return Response(status_message, status_http)
