from django.shortcuts import render
import requests
from decouple import config
import datetime
# Create your views here.
def index(request):
    api_key = config("API_KEY")
    welcome_message = "Hello, welcome to Weather App"
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'houston' + ',' + 'USA', 'appid': api_key}

    #send req to API
    r = requests.get(url=URL,params=PARAMS)
    #fetch respose
    response = r.json()
    #print response object to terminal
    print("resp:", response)
    description= response['weather'][0]['description']
    icon = response['weather'][0]['icon']
    temperature = response['main']["temp"]
    day = datetime.date.today()
    return render(request, 'weatherapp/index.html', {'welcome_message':welcome_message, 'description': description, 'icon':icon, 'temperature':temperature, 'day': day})