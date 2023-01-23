import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

from analysis import *

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#print(vectorize_playlist(sp, 'https://open.spotify.com/playlist/3Zj3Jw5ldyJuTTFa1FanAj?si=2137853538cf4dd7'))


print(get_sound_features(sp, 'https://open.spotify.com/track/0f13ObPdKjihWAb2NY1vkt?si=77681cc50f9b4538'))