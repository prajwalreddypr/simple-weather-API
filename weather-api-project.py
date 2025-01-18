import requests

#api key:  630ecab76aa692c8f137017501c9d97b 
#end point for API calls:  api.openweathermap.org
#example for API call: http://api.openweathermap.org/data/2.5/weather?q=Paris,fr&APPID=630ecab76aa692c8f137017501c9d97b&units=metric

def get_weather(city_name):
    
    api_key = "630ecab76aa692c8f137017501c9d97b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    print(f"The complete URL is: {complete_url}")
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("cod") != 200:                                                      # if NO input or UN RECOGNIZEED input is given.
            print(f"Error: {data.get('message', 'Unable to fetch weather data.')}")
            return None
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to the API. The details are: {e}")
        return None
    
    
def display_weather(data):
    
    if data:
        city = data.get("name")
        country = data.get("sys", {}).get("country")
        temp = data.get("main", {}).get("temp")
        feels_lieke = data.get("main", {}).get("feels_like")
        humidity = data.get("main", {}).get("humidity")                                     #extracts all data from DATA
        weather_desc = data.get("weather", [{}])[0].get("description")
        print(f"\nWeather report for {city}, {country}")
        print("-" * 30)
        print(f"Temperature: {temp} degree celcius")
        print(f"Feels like: {feels_lieke} degree celcius")
        print(f"Humidity is : {humidity}%")
        print(f"Weather summarized: {weather_desc}")
    else:
        print("No weather data to be displayed")
            

if __name__ == "__main__":
    city_name = input("ENter the city name: ")
    weather_data = get_weather(city_name)
    display_weather(weather_data)                              #calls the display_weather function