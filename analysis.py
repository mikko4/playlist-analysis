from collections import defaultdict


def vectorize_playlist(sp, playlist_id):
    """
    Return a vector representing the overall features of a playlist, as a dictionary
    :param sp: spotipy instance
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


def get_sound_features(sp, id):
    """
    Get the audio features of a song given its id
    param sp: spotipy instance
    :param id: id (url, uri, spotify id) of the song
    :return: feature defaultdict
    """
    vect = defaultdict(float)

    for t in sp.audio_features(id):
        for feat in t:
            if feat not in ['type', 'id', 'uri', 'track_href', 'analysis_url']:
                vect[feat] += float(t[feat])

    return vect
