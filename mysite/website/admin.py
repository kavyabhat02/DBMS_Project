from django.contrib import admin
from .models import books_details, librarians, customers, reviews

class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

class LibrarianDetailsAdmin(admin.ModelAdmin):
    list_display = ('librarian_id', 'name')

class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'review', 'rating')

# Register your models here.

admin.site.register(books_details, BookDetailsAdmin)
admin.site.register(librarians, LibrarianDetailsAdmin)
admin.site.register(customers, CustomerDetailsAdmin)
admin.site.register(reviews, ReviewAdmin)