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
    queryset = list()

    lists = list(toReadList.objects.all().values())
    books = list(books_details.objects.all().values())

    for i in range(len(lists)):
       for j in range(len(books)):
            if(lists[i]["isbn_id"] == books[j]["isbn"]):
                queryset.append({**lists[i], **books[j]})

    return JsonResponse(queryset, safe=False)

def reviewView(request):
    rev = list(reviews.objects.all().values())
    books = list(books_details.objects.all().values())
    queryset = list() 

    for i in range(len(rev)):
       for j in range(len(books)):
            if(rev[i]["isbn_id"] == books[j]["isbn"]):
                queryset.append({**rev[i], **books[j]})

    return JsonResponse(queryset, safe=False)

def buyBooksView(request):
    queryset = books_toSell.objects.all()
    return JsonResponse(list(queryset.values()), safe=False)