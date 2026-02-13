import requests

city_name= input('Enter city name:\n')
API_key= '369c65485b867b8f64218f9a6582d161'
url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data=response.json()
    #print(data)
    print('Displaying weather report of',city_name)
    print(data['weather'][0]['description'])
    print('Current temperature is ',data['main']['temp'])
    print('Current temperature feels like',data['main']['feels_like'])
    print(

    )
    print('Humidity is ',data['main']['humidity'])