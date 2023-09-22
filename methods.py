import requests

def get_data(whichData):
    data = requests.get('https://swapi.dev/api/{whichData}')
    return data
