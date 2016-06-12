#-*- conding:utf8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q'].strip()
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20 :
            errors.append('Plesae enter at most 20 charachters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    return render_to_response('search_form.html',{'errors':errors})
        # return HttpResponse('Please submit a search term.')

def search_form(request):
    return render_to_response('search_form.html')
    # if 'q' in request.GET:
    #     message = 'You Searched for: %r' %request.GET['q']
    # else:
    #     message = 'You submiited an empty form.'
    # return HttpResponse(message)