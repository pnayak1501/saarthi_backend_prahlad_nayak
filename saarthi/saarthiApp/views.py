from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from saarthiApp.models import Books
import requests


@csrf_exempt
def create_read_book(request):
    if request.method == 'POST':
        authors = request.POST.get("authors").split(",")
        number_of_pages = int(request.POST.get("number_of_pages"))
        book = Books(name=request.POST.get("name"), isbn=request.POST.get("isbn"), authors=authors, number_of_pages=number_of_pages, publisher=request.POST.get("publisher"), country=request.POST.get("country"), release_date=request.POST.get("release_date"))
        book.save()
        return JsonResponse({"status_code": 201, "status": "success", "data": dict(name=request.POST.get("name"), isbn=request.POST.get("isbn"), authors=authors, number_of_pages=number_of_pages, publisher=request.POST.get("publisher"), country=request.POST.get("country"), release_date=request.POST.get("release_date"))})
    elif request.method == 'GET':
        books = Books.objects.all().values()
        return JsonResponse({"status_code": 200, "status": "success", "data": list(books)})

@csrf_exempt
def update_book(request, id):
    book = Books.objects.get(id = id)
    if(request.POST.get('name')):
        book.name = request.POST.get('name')
    if(request.POST.get('isbn')):
        book.isbn = request.POST.get('isbn')
    if(request.POST.get('authors')):
        authors = request.POST.get("authors").split(",")
        book.authors = authors
    if(request.POST.get('country')):
        book.country = request.POST.get('country')
    if(request.POST.get('number_of_pages')):
        number_of_pages = int(request.POST.get("number_of_pages"))
        book.number_of_pages = number_of_pages
    if (request.POST.get('publisher')):
        book.publisher = request.POST.get('publisher')
    if (request.POST.get('release_date')):
        book.release_date = request.POST.get('release_date')
    book.save()
    book = Books.objects.filter(id=id).values()
    b = Books.objects.get(id = id)
    return JsonResponse({"status_code": 200, "status": "success", "message": "The book "+b.name+" was updated successfully" ,"data": list(book)})

@csrf_exempt
def delete_show_book(request, id):
    if request.method == 'GET':
        book = Books.objects.filter(id=id).values()
        return JsonResponse({"status_code": 200, "status": "success", "data": list(book)})
    elif request.method == 'DELETE':
        book = Books.objects.get(id = id)
        book.delete()
        return JsonResponse({"status_code": 200, "status": "success", "message": "The book "+book.name+" was deleted successfully" ,"data": list()})

def external_book(request):
    key_name = request.GET['name']
    r = requests.get('https://www.anapioficeandfire.com/api/books', params=request.GET)
    return HttpResponse(r)
