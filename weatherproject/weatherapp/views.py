from django.shortcuts import render

# Create your views here.
def index(request):
   str = "sync testing"
    welcome_message = "Hello, welcome to Weather App"
    return render(request, 'weatherapp/index.html', {'welcome_message':welcome_message} )