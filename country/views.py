import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.safestring import SafeString
import requests

from .forms import CountryForm

# Create your views here.


def index(request):
    response = requests.get('https://restcountries.eu/rest/v2/all')
    # transfor the response to json objects
    countries = response.json()

    if request.method== 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            print(request.POST['tags'])
            request.session['tags'] = request.POST['tags']
            return redirect('/detail/')
    else:
        form = CountryForm()

    return render(request, 'index.html', {"countries": countries, "form": form})


@api_view(['GET'])
def get_country(request):
    name = request.session.get('tags')
    response = requests.get('https://restcountries.eu/rest/v2/name/{0}'.format(name))
    country = response.json()
    # print(country['name'])

    return render(request, 'detail.html', {"country":country})

    # return render(request, 'detail.html', {"country": country})