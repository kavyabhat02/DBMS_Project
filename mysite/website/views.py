from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import books_details, ebooks, books_toSell

# Create your views here.

def BookView(request):
    #serializer_class = BooksSerializer
    queryset = books_details.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)

def ebooksView(request):
    #serializer_class = BooksSerializer
    queryset = ebooks.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)

def buyBooksView(request):
    #serializer_class = BooksSerializer
    queryset = books_toSell.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)