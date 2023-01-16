import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def vectorize_playlist(playlist_id):
    """
    Return a vector representing the overall features of a playlist, as a dictionary
    :param playlist_id: id (url, uri, spotify id) of the playlist
    :return: dictionary representing feature vector
    """
    vect = defaultdict(float)

    tracks = []
    pops = []
    for item in sp.playlist_items(playlist_id)['items']:
        tracks.append(item['track']['uri'])
        pops.append(item['track']['popularity'])

    for t in sp.audio_features(tracks):
        for feat in t:
            if feat not in ['type', 'id', 'uri', 'track_href', 'analysis_url']:
                vect[feat] += float(t[feat])

    vect['popularity'] = sum(pops)

    for key in vect.keys():
        vect[key] /= len(tracks)
        vect[key] = round(vect[key], 3)

    return vect


print(vectorize_playlist('https://open.spotify.com/playlist/3Zj3Jw5ldyJuTTFa1FanAj?si=2137853538cf4dd7'))
