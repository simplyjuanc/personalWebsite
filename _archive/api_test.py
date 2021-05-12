
# %%
import requests
from twilio.rest import Client
# %%

account_sid = 'AC47c4eb8ad649ce5feaa3b626ef2c6b51'
auth_token = 'ef07941132001cf37cbd439844238b05'



api_key = 'c981d6ed536a242c91b00afd6d1fefaf'
# city_name = 'London'

lat = '51.507351'
lon = '-0.127758'
units = 'metric'

endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'appid':api_key,
    'lat': lat,
    'lon': lon,
    'units': units,
    'exclude':'current,minutely,daily'
}


response = requests.get(url=endpoint,params=params)
response.raise_for_status()

data = response.json()

 # %%

will_rain = False
for hour in range(0,24):
    if data['hourly'][hour]['weather'][0]['id'] < 800:
        print('Bring an umbrella')
        will_rain = True
        break
# %%


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain! Remember to bring an ☔️",
            to='+447445969543',
            from_=''
        )