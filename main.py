'''
Name: spotify-to-mp3
Author: busby08 (git and replit)
Date: 25-02-2024
Description: For all songs in a spotify playlist, dowload them to mp3,
    if they have not been downloaded before.
'''

import json
import os
import spotipy
import subprocess

# Import the modules that require pip
try:
    from youtube_search import YoutubeSearch
    from pytube import YouTube
except ImportError:
    subprocess.run(['pip', 'install', 'youtube-search'])
    subprocess.run(['pip', 'install', 'pytube'])
    subprocess.run('clear')
    from youtube_search import YoutubeSearch
    from pytube import YouTube

def main() -> None:
    ''' The main function of the program. '''
    
    from spotipy.oauth2 import SpotifyClientCredentials
    
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    
    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    
    for album in albums:
        print(album['name'])

if __name__ == '__main__':
    main()