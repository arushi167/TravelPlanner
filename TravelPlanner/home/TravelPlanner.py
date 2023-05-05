import openai
import requests
import json 
from datetime import datetime, timedelta
from pprint import pprint

class TravelPlanner:
    def __init__(self, prompt, openai_key, openweather_key):
        self.openai_key = openai_key
        self.openweather_key = openweather_key
        self.prompt = f"Figure out the source and destination & days count from this prompt: '{prompt}' and in output, return only json data with 'source', 'dest', 'days' as key and days should be of type integer, make sure to use exactly same key name in json, do not return anyother text except jsondata"
        self.source = None
        self.destination = None
        self.days = None

    def extract_information(self):
        openai.api_key = self.openai_key
        model_engine   = "text-davinci-002"
        prompt = self.prompt
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        message = completions.choices[0].text.strip()
        message = json.loads(message.strip())
        self.source = message["source"]
        self.destination = message["dest"]
        self.days = int(message["days"])

    def get_weather(self):
        base_url = "https://api.openweathermap.org/data/2.5/forecast"
        api_key = self.openweather_key
        source_lat, source_long = self.get_lat_long(self.source)
        destination_lat, destination_long = self.get_lat_long(self.destination)

        # Getting the start date
        start_date = datetime.today().strftime('%Y-%m-%d')

        # Creating an empty dictionary to store the weather data
        weather_data = {}

        # Looping over the number of days to get the weather data for each day
        for i in range(self.days):
            # Creating the API request URL with the required parameters
            source_url = f"{base_url}?lat={source_lat}&lon={source_long}&appid={api_key}&dt={self.days}"
            destination_url = f"{base_url}?lat={destination_lat}&lon={destination_long}&appid={api_key}&dt={self.days}"

            # Sending the API requests and storing the response in the dictionary
            source_response = requests.get(source_url).json()
            destination_response = requests.get(destination_url).json()

            weather_data[i+1] = {
                "source": {
                    "minimum_temperture": source_response['list'][i]['main']['temp_min'],
                    "maximum_temperture": source_response['list'][i]['main']['temp_max'],
                    "pressure": source_response['list'][i]['main']['pressure'],
                    "humidity": source_response['list'][i]['main']['humidity'],
                    "visibility": source_response['list'][i]['visibility'],
                    "wind_speed": source_response['list'][i]['wind']['speed'],
                    "description": source_response['list'][i]['weather'][0]['description'],
                    },
                "destination": {
                    "minimum_temperture": destination_response['list'][i]['main']['temp_min'],
                    "maximum_temperture": destination_response['list'][i]['main']['temp_max'],
                    "pressure": destination_response['list'][i]['main']['pressure'],
                    "humidity": destination_response['list'][i]['main']['humidity'],
                    "visibility": destination_response['list'][i]['visibility'],
                    "wind_speed": destination_response['list'][i]['wind']['speed'],
                    "description": destination_response['list'][i]['weather'][0]['description'],
                    }
            }

        return weather_data, self.source, self.destination

    def get_lat_long(self, location):
        url = "https://api.openweathermap.org/geo/1.0/direct"
        params = {
            "q": location,
            "limit": 1,
            "appid": self.openweather_key
        }
        response = requests.get(url, params=params)
        data = response.json()[0]
        lat = data['lat']
        long = data['lon']
        return lat, long

if __name__ == "__main__":
    # Taking the user input
    user_input = input("Enter your travel plan: ")
    openai_key      = "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"
    openweather_key = "8952bcd6d3eea27abe4dd9fdabc1d03c"

    # Creating an object of the TravelPlanner class and extracting the information
    planner = TravelPlanner(user_input, openai_key, openweather_key)
    planner.extract_information()

    # Getting the weather data and printing it
    weather_data, source, destination= planner.get_weather()
    pprint(weather_data)
