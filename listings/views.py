from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'listings/index.htm')

def listing(request):
    return render(request, 'listings/listing.htm')

def search(request):
    return render(request, 'listings/search.htm')

