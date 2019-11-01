from django.contrib import admin

# Register your models here.
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    fields = ['title', 'sup_category', 'category', 'sub_category', 'body', 'author', 'pub_date', 'views', 'likes', 'slug']
    list_display = ['title', 'pub_date']


admin.site.register(Note, NoteAdmin)

