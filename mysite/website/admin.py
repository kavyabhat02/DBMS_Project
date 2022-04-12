from django.contrib import admin
from .models import books_details, librarians, borrowed_books, customers, overdue_books, reviews

class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

class LibrarianDetailsAdmin(admin.ModelAdmin):
    list_display = ('librarian_id', 'name')

# Register your models here.

admin.site.register(books_details, BookDetailsAdmin)
admin.site.register(librarians, LibrarianDetailsAdmin)