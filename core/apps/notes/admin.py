from django.contrib import admin
from .models import Note

# Register your models here.


# registers the `Note` model with the Django admin site. 
# It tells Django that the `Note` model should be displayed and editable in the admin
# interface.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["note_id", "title", "description", "account"]
