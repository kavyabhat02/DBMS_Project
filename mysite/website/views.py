from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import books_details, ebooks, books_toSell, toReadList, reviews

# Create your views here.

def BookView(request):
    queryset = books_details.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)

def ebooksView(request):
    queryset = ebooks.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)

def listsView(request):
    queryset = toReadList.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)

def reviewView(request):
    queryset = reviews.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)

def buyBooksView(request):
    queryset = books_toSell.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)