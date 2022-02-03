from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def addquestion(request):
    return render(request, 'addquestion.html')

#remove on production
def temp(request):
    return render(request, 'tempo.html')