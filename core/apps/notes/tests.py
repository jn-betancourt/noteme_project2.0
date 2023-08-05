from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
import django.contrib.auth.hashers as hasher

from .models import Note
from ..users.models import NotemeUser

# Create your tests here.


class NoteTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = NotemeUser.objects.create(
            email="juan@mail.com",
            username="juan08",
            first_name="Juan",
            last_name="Betancourt",
            password=hasher.make_password("juanito"),
        )
        Note.objects.create(
            note_id="abc123",
            title="title",
            description="description",
            account=self.user
        )
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

    def test_get(self):
        res = self.client.get("/api/notes/getNotes")
        self.assertEqual(res.status_code, 200)
        # self.assertEqual(res.data["detail"], "No notes to retrieve.")

    def test_post_note(self):
        res = self.client.post(
            "/api/notes/modNotes",
            {"note_id": "123456", "title": "My note", "description": "my description"},
        )
        self.assertEqual(res.status_code, 201)
        # self.assertEqual(res.data["detail"], "note created")

    def test_update_note(self):
        res = self.client.put(
            "/api/notes/modNotes",
            {
                "note_id": "abc123",
                "title": "My new note",
                "description": "my new description",
            },
        )
        self.assertEqual(res.status_code, 200)
        # self.assertEqual(res.data["detail"], "note modified")

    def test_delete_note(self):
        res = self.client.delete(
            "/api/notes/modNotes",
            {
                "note_id": "abc123",
            },
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["detail"], "note deleted")
