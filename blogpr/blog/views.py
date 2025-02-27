from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("This is our Basic Blog!")

def index(request):
    return render(request, 'blog/index.html')