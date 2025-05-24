import requests

state_name = input('Enter your state name: ')
API_key = 'b0eb38b9685dd277b8910725edf0dec6'
url = f'https://api.openweathermap.org/data/2.5/weather?q={state_name}&appid={API_key}&units=metric'

response=requests.get(url)
if response.status_code == 200:
    data=response.json()
    print('Weather is',data['weather'][0]['description'])
    print('Current temperature is',data['main']['temp'])
    print('Current temperature feels like',data['main']['feels_like'])
    print('Humidity is',data['main']['humidity'])