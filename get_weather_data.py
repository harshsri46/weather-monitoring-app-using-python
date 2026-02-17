import requests

city_name = input('Enter city name:\n')
API_key = '369c65485b867b8f64218f9a6582d161'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

try:
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        print('\nDisplaying weather report of', city_name)
        print('Weather:', data['weather'][0]['description'])
        print('Current temperature:', data['main']['temp'], '°C')
        print('Feels like:', data['main']['feels_like'], '°C')
        print('Humidity:', data['main']['humidity'], '%')

    elif response.status_code == 404:
        print("\n❌ City not found. Please enter a valid city name.")

    else:
        print("\n⚠️ Error occurred. Status code:", response.status_code)

except requests.exceptions.ConnectionError:
    print("\n❌ Network error. Please check your internet connection.")

except requests.exceptions.Timeout:
    print("\n❌ Request timed out. Try again later.")

except requests.exceptions.RequestException as e:
    print("\n❌ Something went wrong:", e)
