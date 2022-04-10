from curses.ascii import isblank
from msilib.schema import tables
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class books_details(models.Model): 
    isbn = models.IntegerField(primary_key = True, validators = [MinLengthValidator(10), MaxLengthValidator(10)])
    title = models.TextField()
    summary = models.TextField()
    status = models.TextField()

class librarians(models.Model):
    librarian_id = models.IntegerField(primary_key = True)
    name = models.TextField()
    contact = models.IntegerField(validators = [MaxLengthValidator(10), MinLengthValidator(10)])
    
class borrowed_books(models.Model):
    deadline = models.DateField()
    customer_id = models.IntegerField()
    isbn = models.ForeignKey(books_details, on_delete=CASCADE)

class customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    contact = models.IntegerField(validators = [MaxLengthValidator(10), MinLengthValidator(10)])

class toReadList(models.Model):
    listName = models.TextField()
    isbn = models.ForeignKey(books_details, on_delete=CASCADE)
    customer_id = models.ForeignKey(customers, on_delete=CASCADE)

class overdue_books(models.Model):
    deadline = models.DateField()
    isbn = models.ForeignKey(books_details, on_delete=CASCADE)
    customer_id = models.ForeignKey(customers, on_delete=CASCADE)
    librarian_id = models.ForeignKey(librarians, on_delete=CASCADE)

class reviews(models.Model):
    listName = models.TextField()
    rating = models.IntegerField()
    isbn = models.ForeignKey(books_details, on_delete=CASCADE)

class books_toSell(models.Model):
    isbn = models.ForeignKey(books_details, on_delete=CASCADE)
    title = models.TextField()
    author = models.TextField()
    price = models.IntegerField()

class ebooks(models.Model):
    isbn = models.ForeignKey(books_details, on_delete=CASCADE)
    title = models.TextField()
    author = models.TextField()
    hyperlink = models.TextField()
