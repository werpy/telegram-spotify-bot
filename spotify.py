import requests


def get_track(track):
    url = f"https://api.spotify.com/v1/search?q={track}&type=track"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQBNGpJ4Dxgu7Cj3GN0slx_hjgGE0n8dUc9K7rdubWVfBHkd29rKO9Q5peTnQe_OMXheuAFYVh-lHT2ZImfF80-zZJ9NHnBF4lPK15Wke0cGsH2DdJQtywO7-RlaPw4cSkNmdUqgnH3s0grAKc6Vht8JlAXFF5M'
    }

    response = requests.request("GET", url, headers=headers)

    if len(response.json()['tracks']['items']) > 0:
        return response.json()['tracks']['items'][0]['external_urls']['spotify']

    return 'Простите, но нету такой песни по указаному выше запросе'
