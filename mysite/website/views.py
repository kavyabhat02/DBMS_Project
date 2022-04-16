from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import books_details

# Create your views here.

def BookView(request):
    #serializer_class = BooksSerializer
    queryset = books_details.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)
