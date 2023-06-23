from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from .models import Note
from django.contrib.auth.models import User

# Create your tests here.


class NoteTestCase(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.user = ""
        self.token = ""
        self.client = APIClient()

    def setUp(self) -> None:
        self.user = User.objects.create(
            username="Juan", password="juanito", email="juan@mail.com"
        )
        self.token = Token.objects.get_or_create(user=self.user)[0].key
        return super().setUp()

    def test_get_notes_new_user(self):
        res = self.client.get(
            "/api/notes/getNotes",
            headers={"Authorization": f"Token {self.token}", "id": self.user.id},
        )
        self.assertEqual(res.status_code, 204)

    def test_CRUD_note(self):
        post = self.client.post(
            "/api/notes/modNote",
            {
                "note_id": "f13vd5b1sca1651s",
                "title": "New Note",
                "description": "description",
                "id": self.user.id,
            },
            headers={"Authorization": f"Token {self.token}", "action": "POST"},
        )
        read = self.client.get(
            "/api/notes/getNotes",
            headers={"Authorization": f"Token {self.token}", "id": self.user.id},
        )
        put = self.client.post(
            "/api/notes/modNote",
            {
                "note_id": "f13vd5b1sca1651s",
                "title": "New Note 2",
                "description": "description 2",
                "id": self.user.id,
            },
            headers={"Authorization": f"Token {self.token}", "action": "PUT"},
        )
        remove = self.client.post(
            "/api/notes/modNote",
            {
                "note_id": "f13vd5b1sca1651s",
            },
            headers={"Authorization": f"Token {self.token}", "action": "DELETE"},
        )
        self.assertEqual(post.status_code, 201)
        self.assertEqual(read.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(remove.status_code, 200)
