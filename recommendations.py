import requests
import json

# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQAdaE3ltwtQNS9fKzNeJKIcITjotQKO4KEq0oc10w0C_CELpMi8d277_qbAFvqEDaI5SSFTmSe5GY7H0ZsjmEmFLm4kdSnnAANtlyEUvhz0qivMjFnTWfLB1IPcmvNX7wn9w92FrHZPm4GDunZpX_HPrng_bxrPBqDiX7SUMb9mW8wHaByz53G56QLSLOf2dlKAcxh7Vz7HDw"
user_id = "	12123525012"

# FILTERS
limit= 50
market= "US"
seed_genres= "alt z"
target_danceability= 0.7
target_acousticness = 0.4
uris = [] 
seed_artists = '6bmlMHgSheBauioMgKv2tn' #Powfu
seed_tracks= '4VEEDnEFLI9dUy5QA51rom' #fools (cant help falling in love) by Foster, Sody, Sarcastic Sounds

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
          "name": "Chill Hip Hop",
          "description": "Powfu and 'fools (can't help falling in love)' by Foster, Sody, Sarcastic Sounds",
          "public": True
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

url = response.json()['external_urls']['spotify']
print(response.status_code)

playlist_id = response.json()['id']
#print(playlist_id)
#print(json_response)
endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)