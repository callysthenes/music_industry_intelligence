#/usr/bin/python3
#!pip install spotipy
#!pip install configparser

import configparser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
config = configparser.ConfigParser()
config.read('config.ini')

#store credentials in variables
CLIENT_ID=config['spotify']['client_id']
CLIENT_SECRET=config['spotify']['client_secret']

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


'''artist_name = []
track_name = []
track_popularity = []
artist_id = []
track_id = []'''
for i in range(0,1000,50):
    #track_results = sp.search(q='year:2021-2022', type='track', limit=50,offset=i)
    #track_results = sp.search(q='artist:' + artist + ', album:' + title, type=type, limit=i)
    track_results = sp.search(q='artist:' + 'Beyonce' + ', album:' + 'Lemonade', type='album', limit=1)
print(track_results)
