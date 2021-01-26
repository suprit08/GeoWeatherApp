from django.shortcuts import render
import requests
import logging

import datetime

x = datetime.datetime.now()

startdate = str(x.year)+'-'+x.strftime("%m")+'-'+x.strftime("%d")

enddate = str(x.year)+'-'+x.strftime("%m")+'-'+str(int(x.strftime("%d"))+1)

def home(request):
    return render(request, 'home.html')

def showgeodata(request):
    postal_code = request.GET['postal_code']
    country = request.GET['country']
    response = requests.get('https://api.weatherbit.io/v2.0/history/daily?postal_code='+postal_code+'&country='+country+'&start_date='+startdate+'&end_date='+enddate+'&key=952b420969c0482d856ae42e392f5bcf')
    geodata = response.json()
    
    return render(request, 'geodata.html', {
        'city_name':geodata['city_name'],
        'country_code':geodata['country_code'],
        'datetime': geodata['data'][0]['datetime'],
        'temp': geodata['data'][0]['temp'],
        'avg_pressure' : geodata['data'][0]['pres'],
        'avg_wind_speed' : geodata['data'][0]['wind_spd'],
        'max_temp' : geodata['data'][0]['max_temp'],
        'min_temp' : geodata['data'][0]['min_temp'],
        'max_uv' : geodata['data'][0]['max_uv'],
        'avg_solar_radiation': geodata['data'][0]['solar_rad'],
        'wind_dir': geodata['data'][0]['wind_dir'],
        'clouds': geodata['data'][0]['clouds'],
        'lat': geodata['lat'],
        'lon': geodata['lon'],
    })