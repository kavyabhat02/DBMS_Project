from rest_framework import serializers
from .models import books_details

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_details
        fields = ('isbn', 'title', 'summary', 'status')