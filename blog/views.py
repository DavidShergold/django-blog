from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_blog(request):
    return HttpResponse("Hello, blog!")

