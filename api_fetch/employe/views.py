from django.shortcuts import render
import requests
from django.conf import settings


# Retrive weather data from weather api
def show_data(request):
    api_key = settings.OPENWEATHER_API_KEY  
    city = request.GET.get('city', 'Dhaka')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    dict_data = {}

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dict_data = response.json()
        else:
            dict_data = {"error": f"Failed to fetch data, status code: {response.status_code}"}
    except Exception as e:
        dict_data = {"error": str(e)}

    
    return render(request, 'employe/show.html', {'data': dict_data})

#this is  for my practic api from employes
def check_api(request):
    api_key = "DKWDEL0zYJYl-oN14XEDHllQm6Pp1iqDTq4oVGxEWOM"
    id = request.GET.get('id')

    url = f"http://192.168.0.104:8000/api/v2/employes/?id={id}&appid={api_key}"

    dict_data = {}

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dict_data = response.json()
        else:
            dict_data = {"error": f"Failed to fetch data, status code: {response.status_code}"}
    except Exception as e:
        dict_data = {"error": str(e)}

    return render(request, 'employe/check_api.html', {'data': dict_data})
    

