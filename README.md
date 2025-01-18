# simple-weather-API
The project fetches a simple API call from OpenWeatherMap and displays the desired result.

Displays in the following format:


*****************************************************************
ENter the city name: Paris
The complete URL is: http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=630ecab76aa692c8f137017501c9d97b&units=metric

Weather resport for Paris, FR
------------------------------  
Temperature: 0.07 degree celcius
Feels like: -3.91 degree celcius
Humidity is : 97%
Weather summarized: fog
****************************************************************


If unknown entry:
*****************************************************************
ENter the city name: magicland
The complete URL is: http://api.openweathermap.org/data/2.5/weather?q=magicland&appid=630ecab76aa692c8f137017501c9d97b&units=metric
Error: Unable to connect to the API. The details are: 404 Client Error: Not Found for url: http://api.openweathermap.org/data/2.5/weather?q=magicland&appid=630ecab76aa692c8f137017501c9d97b&units=metric
No weather data to be displayed
*****************************************************************
