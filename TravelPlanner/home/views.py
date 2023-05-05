from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from home.TravelPlanner import TravelPlanner
from pprint import pprint 

# Create your views here.

from django.shortcuts import render, redirect
from django.http import JsonResponse

openai_key      = "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"
openweather_key = "8952bcd6d3eea27abe4dd9fdabc1d03c"

def index(request):
    if request.method == 'POST':
        user_input = request.POST['user_prompt']
        # Creating an object of the TravelPlanner class and extracting the information
        planner = TravelPlanner(user_input, openai_key, openweather_key)
        planner.extract_information()

        # Getting the weather data and printing it
        weather_data, source, destination = planner.get_weather()
        # pprint(weather_data)

        # Make recommendation based on temperature and humidity difference
        temp_diff = abs(weather_data[1]['source']['maximum_temperture'] - weather_data[1]['destination']['maximum_temperture'])
        humid_diff = abs(weather_data[1]['source']['humidity'] - weather_data[1]['destination']['humidity'])
        if temp_diff > 10 and humid_diff > 10:
            recommendation1 = f"It's significantly warmer and more humid in {source} than in {destination}."
            recommendation2 = "You may want to dress accordingly and pack extra water."
        elif temp_diff > 10:
            recommendation1 = f"It's significantly warmer in {source} than in {destination}."
            recommendation2 = "You may want to dress accordingly."
        elif humid_diff > 10:
            recommendation1 = f"It's significantly more humid in {source} than in {destination}."
            recommendation2 = "You may want to pack extra water."
        else:
            recommendation1 = f"The weather in {source} is similar to the weather in {destination}."
            recommendation2 = ""
        recommendations = [recommendation1, recommendation2]

        return render(request, 'index.html', {"data": weather_data, "source": source, "destination": destination, "recommendations": recommendations})

    return render(request, 'index.html')

def signup(request):
    return render(request, "signup.html")

