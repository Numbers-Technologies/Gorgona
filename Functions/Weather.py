# import the module
import python_weather
import asyncio

async def getweather(city):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("Ufa")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature, weather.current.sky_text)
    await client.close()
    return weather.current.temperature

