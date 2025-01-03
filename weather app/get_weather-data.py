import requests
city_name='pune'
API_key='feb45dd3d3a3ed693bab50132baf25a3'
url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data= response.json()
    print('weather is',data['weather'][0]['description'])
    print('tepm :',data['main']['temp'])
    print('feels like :',data['main']['feels_like'])
    print('humidity :',data['main']['humidity'])
print('hhh')

    
