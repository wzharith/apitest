from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    response = requests.get('https://restcountries.eu/rest/v2/all')
    # transfor the response to json objects
    todos = response.json()
    return render(request, 'index.html', {"todos": todos})