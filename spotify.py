# - *- coding: utf- 8 - *-
import requests
import base64
from decouple import config as env_conf


client_id = env_conf('SPOTIFY_CLIENT_ID', cast=str)
client_secret = env_conf('SPOTIFY_CLIENT_SECRET', cast=str)


def get_access_token():
    url = 'https://accounts.spotify.com/api/token'

    base64_token = base64.b64encode(f'{client_id}:{client_secret}'.encode('ascii')).decode('ascii')

    payload={'grant_type': 'client_credentials'}
    headers = {
      'Authorization': f'Basic {base64_token}',
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json()['access_token']



def get_track(track):
    url = f'https://api.spotify.com/v1/search?q={track}&type=track'

    access_token = get_access_token()

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers)

    if len(response.json()['tracks']['items']) > 0:
        return response.json()['tracks']['items'][0]['external_urls']['spotify']

    return 'Простите, но нету такой песни по указаному выше запросе'
