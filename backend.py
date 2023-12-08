import requests


API_KEY = "2c0b123f3bdf5fdb490c26cf19e4f7f9"


def get_data(place, forcast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data
