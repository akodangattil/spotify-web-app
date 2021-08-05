import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys
import pandas as pd
import logging

# SETTINGS 
client_id = "34f1d8f9ba594b6093c9f60f854ab9df"
client_secret = "429af62766754ab9bb213856e9cba8ae"
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQB7dqPasFejYHE3VXXIucOcBc7YAh4v1XpMP_-kJjwMQQ-fA-X_IVPCCuoLAlYw19m-GN9IxqiNykfW8Ouh9jAnmvjOd_b7oq9KZ7p1hUtLhSn79wWw6dqPFdH6cWh5ok5oUCkro-7wWWbbQYPGAfwDzB3-aH5ttVtk-r30wxtR10WHMzgNmufv9clFs_wpbvjB29rxq1BYqkNmy0I1HSVKUUvpiuCXM8EEJUrff7-mUiUjuQVjtiRnCZ7iXRJyBUNPKwHqR1Pbv2pzL3WE9cBP"
user_id = "	12123525012"

logger = logging.getLogger('test.find_artist')
logging.basicConfig(level='INFO')

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

# USER INPUT
limit = input("How many songs would you like on this playlist? ")
#seed_genres = input("What genre? ")
name = input("Please enter an artist: ")
song_name = input("Please enter a song name: ")
playlist_name = input("Please enter the name for this playlist: ")


# FIND ARTIST
results = sp.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
else:
    None

# FIND TRACK
results = sp.search(q='track:' + song_name, type='track')
items = results['tracks']['items']
if len(items) > 0:
  track = items[0]
else:
  None

logger.info('====%s====', artist['name'])
#logger.info('Popularity: %s', artist['popularity'])
#if len(artist['genres']) > 0:
#    logger.info('Genres: %s', ','.join(artist['genres']))
logger.info('====%s====', track['name'])

# FILTERS
market= "US"
target_danceability= 0.7
target_acousticness = 0.4
uris = [] 
seed_artists = artist['id'] 
seed_genres = artist['genres']
seed_tracks= track['id'] 

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&target_acousticness={target_acousticness}'
query += f'&seed_artists={seed_artists}'
query += f'&seed_tracks={seed_tracks}'

response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

#print(json_response)

for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
#print(json_response)
endpoint_url = f"https://api.spotify.com/v1/users/{12123525012}/playlists"

request_body = json.dumps({
          "name": playlist_name,
          "description": "Powfu and 'fools (can't help falling in love)' by Foster, Sody, Sarcastic Sounds",
          "public": True
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

url = response.json()['external_urls']['spotify']
print(response.status_code)

playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)