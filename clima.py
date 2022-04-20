import requests

API_KEY = '7c7bf6251dcffc89cca4a37ebfde2176'


class Weather:
    def __init__(self, city):
        self.city = city

    def __str__(self):
        weather = self.weather_city()

        return f'\nCidade: {weather[0]}\nDescrição: {weather[1]}\nTemperatura: {weather[2]:.1f}ºC\nTemperatura máxima: {weather[3]:.1f}ºC\nTemperatura mínima: {weather[4]:.1f}ºC\n'

    def convert_kelvin(self, temp):
        return temp - 273

    def get_weather(self):
        search = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={API_KEY}&lang=pt_br')

        result = search.json()
        return result

    def weather_city(self):
        result = self.get_weather()

        city = result['name']
        description = result['weather'][0]['description']
        temperature = self.convert_kelvin(result['main']['temp'])
        max_temperature = self.convert_kelvin(result['main']['temp_max'])
        min_temperature = self.convert_kelvin(result['main']['temp_min'])

        return (city, description, temperature, max_temperature, min_temperature)


clima = Weather('New York')
print(clima)
